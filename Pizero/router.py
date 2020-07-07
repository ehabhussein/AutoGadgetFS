from random import randint
from time import sleep
import binascii
import pika
import os
import threading
import select
import argparse
from termcolor import cprint



def showMessage(string,color='green',blink=None):
    """shows messages if error or warn or info"""
    cprint(f"{'*'*(len(string)+4)}\n{string}\n{'*'*(len(string)+4)}",color, attrs=[] if blink is None else ['blink'])


"""check if the gadget is running"""
try:
    fdW = open("/dev/hidg0",'wb')
    hidg = open("/dev/hidg0",'rb')
except FileNotFoundError:
    showMessage("Did you run your gadget? Guess not!\n Quitting...",color="red", blink=1)
    exit(-1)
terminator = 0
mitmcounter = 0

chksimchrNow = ""
chksimchrPrev = ""

def decodePacketAscii(payload=None, rec=None):
    """
    This method decodes packet bytes back to Ascii
    :param payload: bytes of payload to be converted to ascii
    :return: decoded payload
    """
    global chksimchrNow
    global chksimchrPrev
    if rec:
        try:
            chksimchrNow = payload
        except:
            chksimchrNow = binascii.unhexlify(binascii.hexlify(payload))
        chksimchrForm = ""
        for i, s in zip(chksimchrNow, chksimchrPrev):
            try:
                if i == s:
                    chksimchrForm += "\u001B[44m^^\u001B[0m"
                else:
                    chksimchrForm += "\u001B[41m--\u001B[0m"
            except Exception as e:
                pass
        chksimchrPrev = chksimchrNow
    retpayload = ""
    for i in payload:
        decode = chr(ord(chr(i)))
        if decode.isalnum():
            retpayload += decode
        else:
            retpayload += " "
    return retpayload.replace(' ', '.'), chksimchrForm if rec else ""

def makeChannel(ipaddress):
    """creates a channel to RabbitMQ
    :param: ipaddress : ip address of the rabbitmq server
    :return: a channel
    """
    qcreds = pika.PlainCredentials('autogfs', 'usb4ever')
    qpikaparams = pika.ConnectionParameters(ipaddress, 5672, '/',qcreds,heartbeat=60)
    qconnect = pika.BlockingConnection(qpikaparams)
    return qconnect.channel(),qconnect


def mitmProxy(ipaddress, pktlen):
    """reads data from host machine and sends it to the device queue
    :param ipaddress: ip address of the rabbitmq server
    :param ptklen: the device's max packet size
    :return: None
    """
    try:
        cprint("\t[-]Monitoring /dev/hidg0 started!",color="white")
        qchannel2,qconnect2 = makeChannel(ipaddress)
        epoll = select.epoll()
        epoll.register(hidg.fileno(), select.EPOLLIN)
        while True:
            try:
                if terminator == 1:
                    cprint("Cleaning up & exiting..",color="blue")
                    qchannel2.stop_consuming()
                    qconnect2.close()
                    break
                events = epoll.poll(0)
                for fileno, event in events:
                    if event & select.EPOLLIN:
                        packet = hidg.read(pktlen)
                        qchannel2.basic_publish(exchange='agfs', routing_key='todev', body=binascii.hexlify(packet))
                qchannel2.basic_publish(exchange='agfs', routing_key='tonull', body='')
            except KeyboardInterrupt:
                break
            except:
                continue
    except pika.exceptions.StreamLostError:
        cprint("[+]Stream dropped re-initiating Connection to RabbitMQ",color="green")
        cprint("\t[-]Reconnected!",color="white")
        qchannel2,qconnect2 = makeChannel(ipaddress)
    except Exception as e:
            print(e)
            pass


def write2host(ch, method, properties, body):
    """
    writes the data coming from the device to the host
    :param ch:  rabbitMQ channel
    :param method: methods
    :param properties: properties
    :param body: Payload
    :return None
    """
    global mitmcounter
    mitmcounter += 1
    packet,diff = decodePacketAscii(payload=binascii.unhexlify(binascii.hexlify(body)),rec=1)
    cprint(f"|-[From Device]->Write packet->[To Host][Pkt #{mitmcounter}]{'-'*80}", color="green")
    cprint(f"|\t  Bytes:", color="blue")
    cprint(f"|\t\tSent: {binascii.hexlify(body)}",color="white")
    cprint(f"|\t\tDiff:   {diff}", color="white")
    cprint(f"|\t  Decoded:", color="blue")
    cprint(f"|\t\t Sent: {packet}", color="white")
    cprint(f"|{'_'*90}[Pkt #{mitmcounter}]", color="green")
    try:
        os.write(fdW.fileno(),body)
    except Exception as e:
        showMessage("cannot write to fd",color="red",blink=1)
        pass

def fuzzgadgets(ch, method, properties, body):
    vid,pid,dclass,serial,man,prod,min,max = body.decode('utf-8').split("!!")
    chmodgadget = "chmod a+x tempgadget.sh"
    creategadget = "./tempgadget.sh"
    removegadget = "./removegadget.sh"
    cprint("Creating new gadget",color="blue")
    with open('tempgadget.sh','w') as gdt:
        basedir = "/sys/kernel/config/usb_gadget"
        gdt.write("#!/bin/bash\n")
        gdt.write("modprobe libcomposite\n")
        gdt.write("cd /sys/kernel/config/usb_gadget/\n")
        gdt.write("mkdir g && cd g\n")
        gdt.write("mkdir -p /sys/kernel/config/usb_gadget/g/strings/0x409/\n")
        gdt.write("mkdir -p /sys/kernel/config/usb_gadget/g/functions/hid.usb0/\n")
        gdt.write("mkdir -p /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/\n")
        gdt.write("echo %s > %s/g/idVendor\n" % (hex(int(vid)) if vid != "None" else f"0x{binascii.hexlify(os.urandom(2)).decode()}", basedir))
        gdt.write("echo %s > %s/g/idProduct\n" % (hex(int(pid)) if pid != "None" else f"0x{binascii.hexlify(os.urandom(2)).decode()}", basedir))
        gdt.write("echo %s > %s/g/bcdDevice\n" % ("0x200", basedir))
        gdt.write("echo %s > %s/g/bcdUSB\n" % ("0x0058", basedir))
        gdt.write("echo %s > %s/g/bDeviceClass\n" % (hex(int(dclass)) if dclass != "None" else f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        gdt.write("echo %s > %s/g/bDeviceSubClass\n" % (f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        gdt.write("echo %s > %s/g/bDeviceProtocol\n" % (f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        gdt.write("echo %s > %s/g/bMaxPacketSize0\n" % (f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        gdt.write("echo %s > %s/g/strings/0x409/serialnumber\n" % (serial if serial else f"{binascii.hexlify(os.urandom(50))}%c%c%c%s%s%s%d%p", basedir))
        gdt.write("echo '%s' > %s/g/strings/0x409/manufacturer\n" % (man if man != "None" else f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        gdt.write("echo '%s' > %s/g/strings/0x409/product\n" % (prod if prod != "None" else f"0x{binascii.hexlify(os.urandom(50)).decode()}", basedir))
        gdt.write("echo %s > %s/g/configs/c.1/MaxPower\n" % (f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        gdt.write("echo %s > %s/g/configs/c.1/bmAttributes\n" % ("0x80", basedir))
        gdt.write("echo 'Default Configuration' > %s/g/configs/c.1/strings/0x409/configuration\n" % (basedir))
        gdt.write("echo %s > %s/g/functions/hid.usb0/protocol\n" % (f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        gdt.write("echo 256 > %s/g/functions/hid.usb0/report_length\n" % (basedir))
        gdt.write("echo %s > %s/g/functions/hid.usb0/subclass\n" % (f"0x{binascii.hexlify(os.urandom(1)).decode()}", basedir))
        s = f"05010900a1{binascii.hexlify(os.urandom(randint(int(min), int(max)))).decode()}c0"
        gdt.write("echo '%s' | xxd -r -ps > %s/g/functions/hid.usb0/report_desc\n" % (s, basedir))
        gdt.write("ln -s %s/g/functions/hid.usb0 %s/g/configs/c.1\n" % (basedir, basedir))
        gdt.write("udevadm settle -t 5 || :\n")
        gdt.write("ls /sys/class/udc/ > %s/g/UDC\n" % (basedir))
        gdt.close()
    cprint("Running the gadget",color='blue')
    os.system(chmodgadget)
    os.system(creategadget)
    sleep(4)
    cprint("removing the gadget",color='white')
    os.system(removegadget)

def gadgetfuzzer(ipaddress):
    qchannel, qconnect = makeChannel(ipaddress)
    qchannel.basic_consume(on_message_callback=fuzzgadgets, queue='gdtfz', auto_ack=True)
    qchannel.start_consuming()

if __name__ == '__main__':
    try:
        argparse = argparse.ArgumentParser()
        argparse.add_argument('-ip',dest='ipaddress',help='ip address of RabbitMQ', required=True)
        argparse.add_argument('-l',dest='pktlen',help='packet length. Check bMaxPacketsize0 on your device', required=True)
        argparse.add_argument('-s',dest='hstonly',help='Just to receive packets to the host')
        args = argparse.parse_args()
        if not args.hstonly:
            router = threading.Thread(target=mitmProxy, args=(args.ipaddress, int(args.pktlen),))
            router.start()
        cprint("[+]Initiating Connection to RabbitMQ",color="green")
        gdtfuzzer = threading.Thread(target=gadgetfuzzer, args=(args.ipaddress,))
        gdtfuzzer.start()
        while True:
            try:
                qchannel,qconnect = makeChannel(args.ipaddress)
                qchannel.basic_consume(on_message_callback=write2host, queue='tohost',auto_ack=True)
                cprint("\t[-]Started!",color="white")
                cprint("[+]Press Ctrl-C anytime to clean up and exit!",color="green")
                cprint("[+]MITM and gadget fuzzers sessions have started!",color="blue",attrs=['blink'])
                qchannel.start_consuming()
            except KeyboardInterrupt:
                terminator = 1
                qchannel.stop_consuming()
                qconnect.close()
                if not args.hstonly:
                    router.join()
            except:
                continue
    except:
        pass

