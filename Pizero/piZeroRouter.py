import binascii
import sys
import pika
import os
import multiprocessing
from time import sleep
fdW = os.open("/dev/hidg0",os.O_WRONLY)

def mitmproxy(ip,fdR,mode,length):
            qcreds2 = pika.PlainCredentials('autogfs', 'usb4ever')
            qpikaparams2 = pika.ConnectionParameters(sys.argv[1], 5672, '/', qcreds2)
            qconnect2 = pika.BlockingConnection(qpikaparams2)
            qchannel2 = qconnect2.channel()
            while True:
                try:
                        packet = fdR.read(64)
                        #print(packet)
                        qchannel2.basic_publish(exchange='agfs', routing_key='todev' if mode is None else 'tonull',body=binascii.hexlify(packet))
                except Exception as e:
                        qchannel2.basic_publish(exchange='agfs', routing_key='tonull',body="HeartBeat")
                        print(e)
                        pass
                qchannel2.basic_publish(exchange='agfs', routing_key='tonull',body="HeartBeat")

def write2host(ch, method, properties, body):
    #with os.open("/dev/hidg0",mode='wb') as fdW:
        #x = os.open("/dev/hidg0",os.O_WRONLY)
        print("VVV----------------FROM DEVICE\n")
        print(body)
       #fdW.write(body)
        ilen = os.write(fdW,body)
        print(ilen)
        #os.close(x)
        #sleep(0.5)
       # print("^^^----------------FROM DEVICE\n")
        ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    try:
        fdR =  open("/dev/hidg0",mode='rb')
        #print("Starting Router")
        try:
            mode = sys.argv[2]
        except:
            mode = None
        try:
            readlen = int(sys.argv[3])
        except: 
            readlen = 64
        router = multiprocessing.Process(target=mitmproxy, args=(sys.argv[1],fdR,mode,readlen))
        router.start()
        print("Router Started")
        print("Initiating Connection to RabbitMQ")
        qcreds = pika.PlainCredentials('autogfs', 'usb4ever')
        qpikaparams = pika.ConnectionParameters(sys.argv[1], 5672, '/', qcreds)
        qconnect = pika.BlockingConnection(qpikaparams)
        qchannel = qconnect.channel()
        qchannel.basic_qos(prefetch_count=1)
        qchannel.basic_consume(on_message_callback=write2host, queue='tohost')
        print("Starting Consumption of queue")
        qchannel.start_consuming()
        
    except KeyboardInterrupt:
        router.terminate()
        fdR.close()
