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


if __name__ == '__main__':
    try:
        argparse = argparse.ArgumentParser()
        argparse.add_argument('-ip',dest='ipaddress',help='ip address of RabbitMQ', required=True)
        argparse.add_argument('-l',dest='pktlen',help='packet length. Check bMaxPacketsize0 on your device', required=True)
        argparse.add_argument('-s',dest='hstonly',help='Just to receive packets to the host')
        args = argparse.parse_args()
        cprint("[+]Go go gadget MITM!",color="green")
        if not args.hstonly:
            router = threading.Thread(target=mitmProxy, args=(args.ipaddress, int(args.pktlen),))
            router.start()
        cprint("[+]Initiating Connection to RabbitMQ",color="green")
        while True:
            try:
                qchannel,qconnect = makeChannel(args.ipaddress)
       # qchannel.basic_qos(prefetch_count=1)
                qchannel.basic_consume(on_message_callback=write2host, queue='tohost',auto_ack=True)
                cprint("\t[-]Started!",color="white")
                cprint("[+]Press Ctrl-C anytime to clean up and exit!",color="green")
                cprint("[+]MITM session has now started!",color="blue",attrs=['blink'])
                qchannel.start_consuming()
        #cprint("[+]Stream dropped reinitiating Connection to RabbitMQ",color="green")
        #cprint("\t[-]Reconnected!",color="white")
        #qchannel,qconnect = makeChannel(args.ipaddress)
        #qchannel.basic_consume(on_message_callback=write2host, queue='tohost',auto_ack=True)
        #qchannel.start_consuming()
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

