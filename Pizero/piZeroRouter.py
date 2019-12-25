import binascii
import os,sys
import pika
import multiprocessing
from time import sleep

def mitmproxy(ip,fdR):
        try:
            qcreds2 = pika.PlainCredentials('autogfs', 'usb4ever')
            qpikaparams2 = pika.ConnectionParameters(sys.argv[1], 5672, '/', qcreds2)
            qconnect2 = pika.BlockingConnection(qpikaparams2)
            qchannel2 = qconnect2.channel()
            while True:
                packet = fdR.read(64)
                #if packet:
                qchannel2.basic_publish(exchange='agfs', routing_key='todev',body=binascii.hexlify(packet))
        except Exception as e:
            print(e)

def write2host(ch, method, properties, body):
    with open("/dev/hidg0",mode='wb') as fdW:
        print(body)
        s = fdW.write(body)
    print("--------------------------\n")
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    try:
        fdR =  open("/dev/hidg0",mode='rb')
        router = multiprocessing.Process(target=mitmproxy, args=(sys.argv[1],fdR))
        router.start()
        qcreds = pika.PlainCredentials('autogfs', 'usb4ever')
        qpikaparams = pika.ConnectionParameters(sys.argv[1], 5672, '/', qcreds)
        qconnect = pika.BlockingConnection(qpikaparams)
        qchannel = qconnect.channel()
        qchannel.basic_qos(prefetch_count=1)
        qchannel.basic_consume(on_message_callback=write2host, queue='tohost')
        qchannel.start_consuming()

    except KeyboardInterrupt:
        router.terminate()
        #fdR.close()
        #fdW.close()
