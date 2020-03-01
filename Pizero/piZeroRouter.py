from time import sleep
import binascii
import pika
import os
import threading
import select
import argparse

try:
    fdW = open("/dev/hidg0",'wb')
except FileNotFoundError:
    print("Did you run your gadget? Guess not!\n Quitting...")
    exit(-1)
terminator = 0

def makeChannel(ipaddress):
    qcreds = pika.PlainCredentials('autogfs', 'usb4ever')
    qpikaparams = pika.ConnectionParameters(ipaddress, 5672, '/',qcreds)
    qconnect = pika.BlockingConnection(qpikaparams)
    return qconnect.channel()


def mitmProxy(ipaddress, pktlen):
        try:
            print("Monitoring /dev/hidg0 started!")
            qchannel2 = makeChannel(ipaddress)
            with open('/dev/hidg0', 'rb') as hidg:
                epoll = select.epoll()
                epoll.register(hidg.fileno(), select.EPOLLIN)
                while True:
                    if terminator == 1:
                        print("Cleaning up!")
                        break
                    events = epoll.poll(0)
                    for fileno, event in events:
                        if event & select.EPOLLIN:
                            packet = hidg.read(pktlen)
                            qchannel2.basic_publish(exchange='agfs', routing_key='todev', body=binascii.hexlify(packet))
                    qchannel2.basic_publish(exchange='agfs', routing_key='tonull', body='')
        except Exception as e:
            print(e)
            pass


def write2host(ch, method, properties, body):
        print("VVV----------------FROM DEVICE\n")
        print(body)
        os.write(fdW.fileno(),body)


if __name__ == '__main__':
    try:
        argparse = argparse.ArgumentParser()
        argparse.add_argument('-ip',dest='ipaddress',help='ip address of RabbitMQ', required=True)
        argparse.add_argument('-l',dest='pktlen',help='packet length. Check bMaxPacketsize0 on your device', required=True)
        argparse.add_argument('-s',dest='hstonly',help='Just to send packets to the host')
        args = argparse.parse_args()
        print("Go go gadget MITM!")
        if not args.hstonly:
            router = threading.Thread(target=mitmProxy, args=(args.ipaddress, int(args.pktlen),))
            router.start()
        print("Initiating Connection to RabbitMQ")
        qchannel = makeChannel(args.ipaddress)
        #qchannel.basic_qos(prefetch_count=1)
        qchannel.basic_consume(on_message_callback=write2host, queue='tohost',auto_ack=True)
        print("Starting Consumption of queue")
        print("Started!")
        qchannel.start_consuming()
        
    except KeyboardInterrupt:
        terminator = 1
        if not args.hstonly:
            router.join()

