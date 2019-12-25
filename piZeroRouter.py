import binascii
import os,sys
import pika
import multiprocessing

fd = os.open("/dev/hidg0",os.O_RDWR)


def mitmproxy(ip,fd):
        try:
            qcreds2 = pika.PlainCredentials('autogfs', 'usb4ever')
            qpikaparams2 = pika.ConnectionParameters(sys.argv[1], 5672, '/', qcreds2)
            qconnect2 = pika.BlockingConnection(qpikaparams2)
            qchannel2 = qconnect2.channel()
            while True:
                packet = binascii.hexlify(os.read(fd,64))
                if packet:
                    qchannel2.basic_publish(exchange='agfs', routing_key='todev',body=packet)
        except Exception as e:
            print(e)


def write2host(ch, method, properties, body):
    print(str(binascii.unhexlify(body)))
    os.write(fd,binascii.unhexlify(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    try:
        fd = os.open("/dev/hidg0",os.O_RDWR)
        router = multiprocessing.Process(target=mitmproxy, args=(sys.argv[1],fd,))
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
