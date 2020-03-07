from time import sleep
import binascii
import pika
import os
import threading
import select
import argparse

"""check if the gadget is running"""
try:
    fdW = open("/dev/hidg0",'wb')
    hidg = open("/dev/hidg0",'rb')
except FileNotFoundError:
    print("Did you run your gadget? Guess not!\n Quitting...")
    exit(-1)
terminator = 0

def makeChannel(ipaddress):
    """creates a channel to RabbitMQ
    :param: ipaddress : ip address of the rabbitmq server
    :return: a channel
    """
    qcreds = pika.PlainCredentials('autogfs', 'usb4ever')
    qpikaparams = pika.ConnectionParameters(ipaddress, 5672, '/',qcreds)
    qconnect = pika.BlockingConnection(qpikaparams)
    return qconnect.channel(),qconnect


def mitmProxy(ipaddress, pktlen):
        """reads data from host machine and sends it to the device queue
	:param ipaddress: ip address of the rabbitmq server
	:param ptklen: the device's max packet size
	:return: None
	"""
        try:
                print("Monitoring /dev/hidg0 started!")
                qchannel2,qconnect2 = makeChannel(ipaddress)
            #with open('/dev/hidg0', 'rb') as hidg:
                epoll = select.epoll()
                epoll.register(hidg.fileno(), select.EPOLLIN)
                while True:
                    if terminator == 1:
                        print("Cleaning up!")
                        qchannel2.stop_consuming()
                        qconnect2.close()
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
	"""
	writes the data coming from the device to the host
	:param ch:  rabbitMQ channel
        :param method: methods
        :param properties: properties
        :param body: Payload
        :return None	
	"""
	print("VVV----------------FROM DEVICE\n")
	print(body)
	try:
		os.write(fdW.fileno(),body)
	except Exception as e:
		print (e)
		print("cannot write to fd")
		pass

if __name__ == '__main__':
    try:
        argparse = argparse.ArgumentParser()
        argparse.add_argument('-ip',dest='ipaddress',help='ip address of RabbitMQ', required=True)
        argparse.add_argument('-l',dest='pktlen',help='packet length. Check bMaxPacketsize0 on your device', required=True)
        argparse.add_argument('-s',dest='hstonly',help='Just to receive packets to the host')
        args = argparse.parse_args()
        print("Go go gadget MITM!")
        if not args.hstonly:
        	router = threading.Thread(target=mitmProxy, args=(args.ipaddress, int(args.pktlen),))
        	router.start()
        print("Initiating Connection to RabbitMQ")
        qchannel,qconnect = makeChannel(args.ipaddress)
       # qchannel.basic_qos(prefetch_count=1)
        qchannel.basic_consume(on_message_callback=write2host, queue='tohost',auto_ack=True)
        print("Starting Consumption of queue")
        print("Started!")
        qchannel.start_consuming()
        
    except KeyboardInterrupt:
        terminator = 1
        qchannel.stop_consuming()
        qconnect.close()
        if not args.hstonly:
        	router.join()

