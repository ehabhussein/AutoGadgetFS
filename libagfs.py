#!/usr/bin/python3
__author__ = "Ehab Hussein"
__credits__ = ['Josep Pi Rodriguez',    'Dani Martinez']
__version__ = "2.1"
__status__ = "Beta"
__twitter__ = "@0xRaindrop"
##################### Imports
import xmltodict
import platform
import binascii
from sys import exit,stdout
from os import geteuid,urandom
from sqlalchemy import MetaData, create_engine, String, Integer, Table, Column, inspect
import pprint
from time import time,sleep
import json
import threading
import getpass
import paramiko
import random
import EDAP
from termcolor import cprint
import inspect
###################### Pre-Checks

if int(platform.python_version()[0]) < 3:
    print ("Python 2.x or older are not supported. Make sure you are using python3\n")
    exit(-1)
if geteuid() != 0:
    print("Don't forget that this needs root privileges!")
    exit(-1)
if int(platform.uname()[2][0]) < 4:
    print("Seems like you have an incompatible kernel, upgrade to something >= 4.x\nThis might not work properly..You have been warned!!!\n")
    print("GadgetFS might not work!!\n")
try:
    import usb
    import usb.core
    import usb.util
except:
    print ("Seems like you done have pyusb installed.\n[-]install it via pip:\n\t[-]pip3 install pyusb")
    exit(-1)
try:
    import pika
except:
    print("Man in the middle for USB will not work. install pika")

############auto gadgetFS class

class agfs():
    def __init__(self):
        self.showMessage("AutoGadgetFS: USB testing made easy",color="white")
        self.fuzzdevice = 0
        self.fuzzhost = 0
        self.ingui = 0
        self.itshid = 0
        self.edap = EDAP.Probability()
        self.SelectedDevice = None
        self.rabbitmqserver = input("Enter IP address of the rabbitmq server: ")

    def createctrltrsnfDB(self):
        """
        creates a SQLite database containing values that were enumerated from control transfer enumeration
        devEnumCtrltrnsf(self,fuzz="fast")
        :return: db and table
        """
        try:
            meta = MetaData()
            db = create_engine('sqlite:///devEnumCT/%s.db' %(self.SelectedDevice))
            db.echo = False
            self.devECT = Table(
            self.SelectedDevice,
            meta,
            Column('bmRequest', String),
            Column('bRequest', String),
            Column('wValue', String),
            Column('wIndex', String),
            Column('Data_length', String),
            Column('Data_returned', String),
            Column('Data_returned_Ascii', String))
            meta.create_all(db)
            return db, self.devECT
        except Exception as e:
            print(e)
            print("[Error] cannot create db\n")

    def createdb(self, name):
        """
        create the sqlite table and columns from usblyzer captures
        :param name: this receives a name for the database name to be created
        """
        try:
            meta = MetaData()
            db = create_engine('sqlite:///%s.db' %(name.strip()))
            db.echo = False
            self.usblyzerdb = Table(
            name.strip(),
            meta,
            Column('Type',String),
            Column('seq', Integer),
            Column('io', String),
            Column('cie', String),
            Column('Duration', String),
            Column('DevObjAddr', String),
            Column('irpaddr', String),
            Column('RawDataSize', Integer),
            Column('RawData', String),
            Column('RawBinary',String),
            Column('replyfrom', Integer))
            meta.create_all(db)
            return db, self.usblyzerdb
        except:
            print("[Error] cannot create db\n")

    def releasedev(self):
        """releases the device and re-attaches the kernel driver"""
        print("[-] Releasing the Interface")
        for configurations in self.device:
            print("Releasing interfaces :\n\t%s" % configurations.bNumInterfaces)
            print("[-] Attaching the kernel driver")
            for inter in range(configurations.bNumInterfaces + 1):
                try:
                    usb.util.release_interface(self.device, inter)
                    print("Releasing interface: %d" % inter)
                    self.device.attach_kernel_driver(inter)
                    print("Interface reattached")
                except:
                    pass
        print("[-] Device released!")

    def deviceInfo(self):
        """gets the complete info only for any usb connected to the host"""
        getusbs = usb.core.find(find_all=True)
        devices = dict(enumerate(str(dev.manufacturer) + ":" + str(dev.idProduct) + ":" + str(dev.idVendor) for dev in getusbs))
        for key, value in devices.items():
            print(key, ":", value)
        hook = input("---> Select a device: ")
        idProd, idVen = devices[int(hook)].split(':')[1:]
        device = usb.core.find(idVendor=int(idVen), idProduct=int(idProd))
        print(device)


    def deviceInterfaces(self):
        """get all interfaces and endpoints on the device"""
        self.device = usb.core.find(idVendor=self.device.idVendor, idProduct=self.device.idProduct)
        self.leninterfaces = 0
        for cfg in self.device:
            print("Configuration Value: "+str(int(cfg.bConfigurationValue)) + '\n')
            for intf in cfg:
                if intf.bInterfaceClass == 3:
                    self.itshid = 1
                self.leninterfaces += 1
                print('\tInterface number: ' + \
                                 str(int(intf.bInterfaceNumber)) + \
                                 ',Alternate Setting: ' + \
                                 str(intf.bAlternateSetting) + \
                                 '\n')
                for ep in intf:
                    print('\t\tEndpoint Address: ' + \
                                     hex(ep.bEndpointAddress) + \
                                     '\n')

    def newProject(self):
        """ creates a new project name if you were testing something else"""
        try:
            self.releasedev()
        except:
            pass
        self.SelectedDevice = None
        self.findSelect()

    def findSelect(self):
        """This method enumerates all USB devices connected and allows you to select it as a target device as well as its endpoints"""
        projname = self.SelectedDevice if self.SelectedDevice else input("Give your project a name?!: ")
        self.getusbs = usb.core.find(find_all=True)
        self.devices = dict(enumerate(str(dev.manufacturer)+":"+str(dev.idProduct)+":"+str(dev.idVendor) for dev in self.getusbs))
        for key,value in self.devices.items():
            print(key,":",value)
        self.hook = input("---> Select a device: ")
        self.idProd,self.idVen = self.devices[int(self.hook)].split(':')[1:]
        self.device = usb.core.find(idVendor=int(self.idVen),idProduct=int(self.idProd))
        print(str(self.device))
        detachKernel = str(input("do you want to detach the device from it's current system driver: [y/n] "))
        if detachKernel.lower() == 'y':
            self.device.reset()
            try:
                """https://stackoverflow.com/questions/23203563/pyusb-device-claimed-detach-kernel-driver-return-entity-not-found"""
                confer = 1
                for configurations in self.device:
                    print("Disabling Interfaces on configuration: %d" %confer)
                    print("Disabling interfaces :\n\t%s" %configurations.bNumInterfaces)
                    for inter in range(configurations.bNumInterfaces+1):
                        try:
                            if self.device.is_kernel_driver_active(inter):
                                self.device.detach_kernel_driver(inter)
                                print("Disabled interface: %d" %inter)
                        except:
                            pass
                print("[-] Kernel driver detached")
                self.device.set_configuration()
            except Exception as e:
                    print("Failed to detach the kernel driver from the interfaces.",e)
        self.deviceInterfaces()
        if input("Do you want to reset the device? [y/n]: ").lower() == 'y':
            self.device.reset()
        try:
            self.precfg = int(input("which Configuration would you like to use: "))

            self.device.set_configuration(self.precfg)
            self.devcfg = self.device.get_active_configuration()
            self.interfacenumber = int(input("which Interface would you like to use: "))
            self.Alternate = int(input("which Alternate setting would you like to use: "))
            self.epin = int(input("which Endpoint IN would you like to use: "), 16)
            self.epout = int(input("which Endpoint OUT would you like to use: "), 16)
            self.interfaces = self.devcfg[(self.interfacenumber, self.Alternate)]
            self.killthread = 0
            print("Checking if device supports DFU mode based on USB DFU R1.1")
            '''based on USB Device Firmware Upgrade Specification, Revision 1.1'''
            dfu = 0
            for i,configurations in enumerate(self.device):
                for j,interface in enumerate(configurations.interfaces()):
                    if interface.bInterfaceClass == 0xFF:
                        print(f"Configuration #{i+1} on interface #{j} needs vendor specific Drivers")
                    if interface.bInterfaceClass == 0xFE and interface.bInterfaceSubClass == 0x01:
                        print(f"This Device supports DFU mode on configuration {i+1}, interface {j}")
                        dfu += 1
            if dfu == 0:
                self.showMessage("This Device doesnt support DFU mode",color="green")
        except Exception as e:
            print(e)
            self.showMessage("Couldn't get device configuration!",color="red",blink='y')

        claim = str(input("Do you want to claim the device interface: [y/n] "))
        if claim.lower() == 'y':
                usb.util.claim_interface(self.device, self.interfaces.bInterfaceNumber)
                if self.itshid == 1:
                    print("Checking HID report retrieval\n")
                    try:
                        self.device_hidrep = []
                        """Thanks https://wuffs.org/blog/mouse-adventures-part-5
                        https://docs.google.com/viewer?a=v&pid=sites&srcid=bWlkYXNsYWIubmV0fGluc3RydW1lbnRhdGlvbl9ncm91cHxneDo2NjBhNWUwNDdjZGE1NWE1
                        """
                        for i in range(0,self.leninterfaces+1):
                            try:
                                #we read the max possible size of a hid report incase the device leaks some data .. it does happen.
                                response = binascii.hexlify(self.device.ctrl_transfer(0x81,0x6,0x2200,i, 0xfff))
                                self.device_hidrep.append(response)
                            except usb.core.USBError:
                                pass
                        if self.device_hidrep:
                            print(self.device_hidrep[0])
                            print(self.decodePacketAscii(binascii.unhexlify(self.device_hidrep[0])))
                            if binascii.unhexlify(self.device_hidrep[0])[-1] != 192 and len(self.device_hidrep) > 0:
                                self.showMessage("Possible data leakage detected in HID report!",color='blue',blink='y')

                        else:
                            self.device_hidrep = []
                    except Exception as e:
                        print (e)
                        self.device_hidrep = []
                        self.showMessage("Couldn't get a hid report but we have claimed the device.",color='red',blink='y')
                self.itshid = 0
        if type(self.device.manufacturer) is type(None):
            self.manufacturer = "UnkManufacturer"
        else:
            self.manufacturer = self.device.manufacturer
        self.SelectedDevice = self.manufacturer + "-" + str(self.device.idVendor) + "-" + str(self.device.idProduct) + "-" + str(time())
        self.SelectedDevice = projname+"-"+self.SelectedDevice.replace(" ",'')
        cloneit = input("Do you want to save this device's information?[y/n]")
        if cloneit.lower() == 'y':
            self.clonedev()

    def monInterfaceChng(self,ven,prod):
        """Method in charge of monitoring interfaces for changes this is called from def startMonInterfaceChng(self)
        don't call this method directly use startMonInterfaceChng(self) instead
        :param ven: receives the vendorID of the device
        :param prod: receives the productID of the device
        :return: None
        """
        temp = str(self.device)
        while True:
                try:
                    if self.monIntKill == 1:
                        break
                    device = usb.core.find(idVendor=ven, idProduct=prod)
                    if temp != str(device):
                        temp = str(device)
                        self.showMessage("Device Interfaces have changed!",color='blue',blink='y')
                    sleep(10)
                except Exception as e:
                    print(e)

    def startMonInterfaceChng(self):
        """This method Allows you to monitor a device every 10 seconds in case it suddenly changes its interface configuration.
        Like when switching and Android phone from MTP to PTP . you'll get a notification so you can check
        your interfaces and adapt to that change using changeintf() method
        """
        self.showMessage("Interface monitoring thread has started.",color='green')
        self.monIntKill = 0
        self.monIntThread = threading.Thread(target=self.monInterfaceChng,args=(self.device.idVendor,self.device.idProduct,))
        self.monIntThread.start()

    def stopMonInterfaceChang(self):
        """Stops the interface monitor thread"""
        self.monIntKill = 1
        self.monIntThread.join()
        self.showMessage("Monitoring of interface changes has stopped",color='green')

    def stopSniffing(self):
        """Kills the sniffing thread strted by startSniffReadThread()"""
        self.killthread = 1
        self.readerThread.join()
        try:
            self.bintransfered.close()
        except:
            pass
        try:
            self.genpktsF.close()
        except:
            pass
        if self.frompts == 0:
            try:
                self.qchannel3.stop_consuming()
            except:
                pass
            self.qconnect3.close()
        self.showMessage("Sniffing has stopped successfully!",color='green')
        self.killthread = 0

    def startSniffReadThread(self,endpoint=None, pts=None, queue=None,timeout=0,genpkts=0):
        """ This is a thread to continuously read the replies from the device and dependent on what you pass to the method either pts or queue
       :param endpoint: endpoint address you want to read from
       :param pts: if you want to read the device without queues and send output to a specific tty
       :param queue: if you will use the queues for a full proxy between target and host
       :param channel: this is automatically passed if you use the self.startMITMusbWifi()
       :param savetofile: fill in ********************
       :param genpkts: fill in ********************
       :return: None
       """
        mypts = None
        self.killthread = 0
        if queue is not None:
            self.frompts = 0
            self.qcreds3 = pika.PlainCredentials('autogfs', 'usb4ever')
            self.qpikaparams3 = pika.ConnectionParameters(self.rabbitmqserver, 5672, '/',  self.qcreds3,heartbeat=60)
            self.qconnect3 = pika.BlockingConnection(self.qpikaparams3)
            self.qchannel3 = self.qconnect3.channel()
        if pts is not None:
            self.frompts = 1
            mypts = input("Open a new terminal and type 'tty' and input the pts number: (/dev/pts/X) ")
            input("Press Enter when ready..on %s" % mypts)
        self.readerThread = threading.Thread(target=self.sniffdevice, args=(endpoint, mypts, queue, timeout,genpkts))
        self.readerThread.start()

    def sniffdevice(self, endpoint, pts, queue,timeout, genpkts):
        """ read the communication between the device to hosts
        you can either choose set pts or queue but not both.s
       :param endpoint: endpoint address you want to read from)
       :param pts: if you want to read the device without queues and send output to a specific tty
       :param queue: is you will use the queues for a full proxy between target and host
       :param channel: rabbitmq channel
       :param genpkts: write sniffed packets to a file
       :return: None
        """
        if genpkts == 1:
            self.genpktsF = open(f'binariesdb/{self.SelectedDevice}-device.bin','wb')
        if queue and pts is None:
            self.showMessage("Sniffing the device started, messages sent to host queue!",color="green")
            while True:
                if self.killthread == 1:
                    queue = None
                    self.showMessage("Thread Terminated Successfully",color='green')
                    break
                try:
                    packet = self.device.read(endpoint, self.device.bMaxPacketSize0)
                    try:
                        if self.fuzzhost == 1:
                            s = memoryview(binascii.unhexlify(binascii.hexlify(packet))).tolist()
                            random.shuffle(s)
                            packet = binascii.unhexlify(''.join(format(x, '02x') for x in s))
                        if genpkts == 1:
                            self.genpktsF.write(binascii.hexlify(packet))
                            self.genpktsF.write(b'\r\n')

                    except Exception as e:
                        print(e)
                        pass
                    self.qchannel3.basic_publish(exchange='agfs', routing_key='tohst',
                                                 body=packet)

                except usb.core.USBError as e:
                    if e.args == ('Operation timed out\r\n',):
                        self.showMessage("Operation timed out cannot read from device",color='red',blink='y')
                    pass
                except Exception as e:
                    print(e)
                    self.showMessage("Error read from device",color='red')
                self.qchannel3.basic_publish(exchange='agfs', routing_key='tonull',body="heartbeats")
                #sleep(1)
        elif pts and queue is None:
            with open('%s'%(pts.strip()), 'w') as ptsx:
                while True:
                    if self.killthread == 1:
                        pts = None
                        ptsx.write("Thread Terminated Successfully")
                        break
                    try:
                            packet = binascii.hexlify(self.device.read(endpoint, self.device.bMaxPacketSize0))
                            ptsx.write(f"{binascii.unhexlify(packet)}\r\n-----------------^^^FROM DEVICE^^^----------------\r\n")
                            ptsx.flush()
                            if genpkts == 1:
                                self.genpktsF.write(packet)
                                self.genpktsF.write(b'\r\n')
                    except usb.core.USBError as e:
                        if e.args == ('Operation timed out! Cannot read from device\n',):
                            ptsx.write("Operation timed out! Cannot read from device\n")
                            ptsx.flush()
                        pass
        else:
            self.showMessage("either pass to a queue or to a tty",color='red',blink='y')

    def startMITMusbWifi(self,endpoint=None,savefile=None,genpkts=0):
        """ Starts a thread to monitor the USB target Device
        :param endpoint: the OUT endpoint of the device most probably self.epout which is from the device to the PC
        :param savefile: if you would like the packets from the host to be saved to a binary file
        :param: genpkts: save packets from device to file
        :return: None
        """
        if savefile:
            self.savefile = 1
        self.killthread = 0
        self.startMITMProxyThread = threading.Thread(target=self.MITMproxy, args=(endpoint,savefile,genpkts))
        self.startMITMProxyThread.start()

    def stopMITMusbWifi(self):
        ''' Stops the man in the middle thread between the host and the device'''
        try:
            if self.savefile:
                self.bintransfered.close()
        except:
            pass
        self.stopSniffing()
        self.savefile = None
        self.killthread = 1
        try:
            self.qchannel.stop_consuming()
            self.qconnect.close()
        except:
            pass
        self.startMITMProxyThread.join()
        self.showMessage("MITM Proxy has now been terminated!",color='green')

    def MITMproxyRQueues(self, ch, method, properties, body):
        """
        This method reads from the queue todevice and send the request to the device its self.
        :param ch:  rabbitMQ channel
        :param method: methods
        :param properties: properties
        :param body: Payload
        :return None
        """
        print("VVV++++++++++++++++FROM HOST\n", binascii.unhexlify(body))
        if self.fuzzdevice == 1:
            packet = memoryview(binascii.unhexlify(body)).tolist()
            random.shuffle(packet)
            body = ''.join(format(x, '02x') for x in packet)
            #print("payload shuffled->", packet)
            print("+++++++++++++++^^ manipulated payload^^++++++++++++++++++++++++++++++")
        self.device.write(self.epout, binascii.unhexlify(body))
        try:
            if self.savefile:
                self.bintransfered.write(body)
                self.bintransfered.write(b'\r\n')
            #sleep(0.5)
        except Exception as e:
            pass
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def MITMproxy(self,endpoint,savetofile,genpkts):
        """
        :param endpoint: the IN endpoint
        :return: None
        """
        try:
            try:
                if savetofile:
                    self.savefile = 1
                    self.bintransfered = open(f"binariesdb/{self.SelectedDevice}-Host.bin",'wb')
            except:
                self.savefile = None
            self.qcreds = pika.PlainCredentials('autogfs', 'usb4ever')
            self.qpikaparams = pika.ConnectionParameters(self.rabbitmqserver, 5672, '/', self.qcreds)
            self.qconnect = pika.BlockingConnection(self.qpikaparams)
            self.qchannel = self.qconnect.channel()
            #self.qchannel.basic_qos(prefetch_count=1)
            self.qchannel.basic_consume(on_message_callback=self.MITMproxyRQueues, queue='todevice')
            self.startSniffReadThread(endpoint=self.epin, queue=1,genpkts=genpkts)
            print("Connected to RabbitMQ, starting consumption!")
            print("Connected to exchange, we can send to host!")
            self.qchannel.start_consuming()
            self.showMessage("MITM Proxy stopped!",color="green")
        except Exception as e:
            print(e)

    def devWrite(self,endpoint,payload):
        """To use this with a method you would write make sure to run the startSniffReadThread(self,endpoint=None, pts=None, queue=None,channel=None)
         method first so you can monitor responses
        :param endpoint: endpoint address you want to write method
        :param payload: the message to be sent to the devices
        :return: None
        """
        self.device.write(endpoint,payload)

    def devctrltrnsf(self,bmRequestType, bRequest, wValue, wIndex, wLength):
        """ This method allows you to send ctrl transfer requests to the target device
        Usually you'll find the parameters for this method in the vendor's data sheet.
        https://www.beyondlogic.org/usbnutshell/usb6.shtml
        :param bmRequestType: direction of the request
        :param bmRequest: determines the request being made
        :param wValue: parameters to be passed with the request
        :param wIndex: parameters to be passed with the request
        :param wLength: Number of bytes to transfer if there is a data phase
        """
        print(binascii.hexlify(self.device.ctrl_transfer(bmRequestType,bRequest,wValue,wIndex,wLength)))

    def startQueuewrite(self):
        """initiates a connection to the queue to communicate with the host"""
        self.hbkill = 0
        self.qcreds3 = pika.PlainCredentials('autogfs', 'usb4ever')
        self.qpikaparams3 = pika.ConnectionParameters(self.rabbitmqserver, 5672, '/',  self.qcreds3,heartbeat=60)
        self.qconnect3 = pika.BlockingConnection(self.qpikaparams3)
        self.qchannel3 = self.qconnect3.channel()
        self.showMessage("Queues to host are yours!",color='blue')

    def stopQueuewrite(self):
        """ stop the thread incharge of communicating with the host machine"""
        #self.qchannel3.stop_consuming()
        self.qconnect3.close()

    def clearqueues(self):
        """this method clears all the queues on the rabbitMQ queues that are set up"""
        self.qcreds4 = pika.PlainCredentials('autogfs', 'usb4ever')
        self.qpikaparams4 = pika.ConnectionParameters(self.rabbitmqserver, 5672, '/',self.qcreds4,heartbeat=60)
        self.qconnect4 = pika.BlockingConnection(self.qpikaparams4)
        self.qchannel4 = self.qconnect4.channel()
        self.qchannel4.queue_purge('todevice')
        print("cleared todevice queue")
        self.qchannel4.queue_purge('tohost')
        print("cleared tohost queue")
        self.qchannel4.queue_purge('tonull')
        print("cleared tonull queue")
        self.qchannel4.queue_purge('edapdev')
        self.qchannel4.queue_purge('edaphst')
        print("cleared edap queues")
        self.qconnect4.close()

    def hostwrite(self, payload, isfuzz=0):
        """ This method writes packets to the host either targeting a software or a driver in control of the device
        use this when you want to send payloads to a device driver on the host

        :param payload: the message to be sent to the host example: "0102AAFFCC"
        :param isfuzz: is the payload coming from the fuzzer ?
        start the pizeroRouter.py with argv[2] set to anything so we can send the host messages to a null Queue
        """
        self.qchannel3.basic_publish(exchange='agfs', routing_key='tohst',
                                     body=binascii.unhexlify(payload) if isfuzz == 0 else payload)

    def hstrandfuzz(self, howmany=1, size=None, min=None, max = None, timeout=0.5):
        """
        this method allows you to create fixed or random size packets created using urandom and send them to the host queue
        :param howmany: how many packets to be sent to the device`
        :param size: fixed size packet length
        size = 10 to generate a length 10 packet
        :param min minimum size value to generate a packet
        :param max maximum size value to generate a packet
        :param timeout: timeOUT !
        :return: None
        """
        self.startQueuewrite()
        sleep(1)
        for i in range(howmany):
            try:
                print("****************VVV Packet #%d  VVV**********************" % i)
                if size:
                    s = urandom(size)
                    print("sent-->\n", binascii.hexlify(s))
                    self.hostwrite(s,isfuzz=1)
                elif min is not None and max is not None:
                    s = urandom(random.randint(min, max))
                    print("sent-->\n", binascii.hexlify(s))
                    self.hostwrite(s, isfuzz=1)
                sleep(timeout)
            except Exception as e:
                self.showMessage("Error -->sending packet\n",color='red',blink='y')
                pass
        self.stopQueuewrite()

    def devrandfuzz(self, howmany=1000, size='fixed',timeout=0.5):
        """
        this method allows you to create fixed or random size packets created using urandom
        :param howmany: how many packets to be sent to the device`
        :param size: string value whether its fixed or random size
        :param timeout: timeOUT !
        :return: None
        """
        for i in range(howmany):
                try:
                    if size == 'fixed':
                        s = urandom(self.device.bMaxPacketSize0)
                    else:
                        s = urandom(random.randint(0, self.device.bMaxPacketSize0))
                    self.device.write(self.epout, s)
                    r = self.device.read(self.epin, self.device.bMaxPacketSize0)
                    sdec = self.decodePacketAscii(s)
                    rdec = self.decodePacketAscii(r)
                    cprint(f"|-Packet[{i}]{'-'*80}", color="green")
                    cprint(f"|\t  Bytes:", color="blue")
                    cprint(f"|\t\tSent: {binascii.hexlify(s)}\n|\t\t    |____Received: {binascii.hexlify(r)}", color="white")
                    cprint(f"|\t  Decoded:", color="blue")
                    cprint(f"|\t\t Sent: {sdec}\n|\t\t    |____Received: {rdec}", color="white")
                    cprint(f"|{'_'*90}[{i}]", color="green")
                    sleep(timeout)
                except usb.core.USBError as e:
                    cprint(f"|-Packet[{i}]{'-'*80}", color="red", attrs=['blink'])
                    cprint(f"|\t  Error:", color="red") #not blinking to grab attention
                    cprint(f"|\t\tSent: {binascii.hexlify(s)}",color='red', attrs=['blink'])
                    cprint(f"|\t\t|____{e}", color='red', attrs=['blink'])
                    cprint(f"|{'_'*90}[{i}]", color="red", attrs=['blink'])
                    pass

    def devSmartFuzz(self,engine=None,samples=100,direction=None,filename=None,fromQueue=None):
        """
        This method is generates packets based on what it has learned from a sniff from either the host or the device
        :param engine: choice between smart, random , patterns
            random: [truly random based on charset , length , chars found]
            smart: [based on input , weight & positions]
            patterns: [based on smart + char cases]
        :param samples: number of samples to be generated
        :param direction: 'hst' or 'dev'
        :param filename: 'filename to learn from'
        :return: self.edap.packets: packets generated
        """
        if filename is not None:
            self.edap.readwords =list(set([i.decode('utf-8').strip() for i in open(filename, 'rb')]))
        elif fromQueue is not None:
            self.edap.readwords = fromQueue
        else:
            return "nothing to do"
        self.edap.charset = list()
        self.edap.alphaupperindexes = list()
        self.edap.alphalowerindexes = list()
        self.edap.integerindexes = list()
        self.edap.nonalphanumindexes = list()
        self.edap.frequencies = dict()
        self.edap.fullkeyboard = list("`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?")
        self.edap.discardedcharset = list()
        self.edap.finalcharset = list()
        self.edap.countUpper = 0
        self.edap.countLower = 0
        self.edap.countDigits = 0
        self.edap.countOther = 0
        self.edap.pppc = 1
        self.edap.word_dct = dict()
        self.edap.packets = []
        self.edap.howmany = samples
        self.edap.unusedindexes = list(range(len(max(self.edap.readwords, key=len).strip())))
        self.edap.getcharset()
        self.edap.getindexes()
        self.edap.printgeneralstats()
        self.edap.frequency_index_vertical()
        self.edap.frequency_index_horizontal()
        self.edap.charswithfriendswithwords()
        self.edap.PrefinalAnalysis()
        if engine == "smart":
            for i in range(samples):
                self.edap.smartGenerator()
        elif engine == "patterns":
            for i in range(samples):
                self.edap.patterngenerator()
        if engine == "random":
            self.edap.randomgenerator()
        self.showMessage(f"generated:{len(self.edap.packets)} Packets",color='green')
        return self.edap.packets

    def devbrutefuzz(self, starter=0x00,ranger=0xffffffffff+1,timeout=0):
        """
        This method allows you to create sequencial increment packets and send them to the device
        :param starter: start value to bruteforce from in hex notation
        :param ranger: end value where the bruteforce ends in hex notation
        :param timeout: timeout!
        :return:  none
        """
        '''https://stackoverflow.com/questions/46739981/ways-to-increment-hex-in-python?rq=1'''
        for i,j in enumerate(range(starter,ranger)):
            try:
                print("****************VVV Packet #%d  VVV**********************" %i)
                makebytes= j.to_bytes((j.bit_length() + 7) // 8 or 1, 'big')
                s = binascii.unhexlify(binascii.hexlify(makebytes).ljust(self.device.bMaxPacketSize0*2, b'0'))
                self.device.write(self.epout, s)
                print("sent-->\n", binascii.hexlify(s))
                print("received -->\n",
                      binascii.hexlify(self.device.read(self.epin, self.device.bMaxPacketSize0).tobytes()))
                sleep(timeout)
            except usb.core.USBError as e:
                print(e)
                self.showMessage("received --> Timed Out\n",color='red',blink='y')
                pass

    def devEnumCtrltrnsf(self,fuzz="fast"):
        """
        This method enumerates all possible combinations of a control transfer request
        :param fuzz: "fast" fuzzer (bmRequest is fuzzed against 0x81 and 0xc0 and the other parameters are limited to one byte
                     "full" fuzzing (bmRequest is range(0xff) , wValue is range(0xffff) , wIndex is range(0xffff) . USE WITH CARE !!
        :return: None
        """
        self.devECTdbObj, _table = self.createctrltrsnfDB()
        self.CTconnection = self.devECTdbObj.connect()
        self.CTtransaction = self.CTconnection.begin()
        self.showMessage("started",color='green')
        nextwInd = 0
        bRequest = 0xff
        if fuzz == "full":
            bm_request = [0x2,0x21,0xA1,0x80,0xC0,0x00,0x81,0x1,0x82]
            wValue = 0xffff
            wIndex = 0xffff
        else:
            bm_request = [0x81, 0xC0]
            wValue = 0xff
            wIndex = 0xff
        dlen = 10
        for i in bm_request:
            self.showMessage(f"Now at bmRequest {hex(i)}",color="blue",blink='y')
            for j in range(bRequest+1):
                for q in range(wValue+1):
                    for w in range(wIndex+1):
                        if nextwInd == 1:
                            nextwInd = 0
                            break
                        for l in range(dlen):
                            try:
                                try:
                                    responder = self.device.ctrl_transfer(i,j,q,w,l)
                                except:
                                    responder = self.device.ctrl_transfer(i, j, q, w)
                                stdout.write("*******************************\nFound Valid Control Transfer request on device: %s" %self.SelectedDevice)
                                stdout.write("\n")
                                stdout.write("bmRequest=0x{0:02X}, bRequest=0x{1:02X},wValue=0x{2:04X} , wIndex=0x{3:02X}, data_length=0x{4:02X}".format(i,j,q,w,l))
                                stdout.write("\n")
                                stdout.write(f"received: {binascii.unhexlify(binascii.hexlify(responder.tobytes()))[:10]}...[SNIP]")
                                stdout.write("\n")
                                stdout.flush()
                                try:
                                    _insert = _table.insert().values(
                                        bmRequest=i,
                                        bRequest=j,
                                        wValue=q,
                                        wIndex=w,
                                        Data_length=len(binascii.unhexlify(binascii.hexlify(responder.tobytes()))),
                                        Data_returned=binascii.unhexlify(binascii.hexlify(responder.tobytes())),
                                        Data_returned_Ascii=self.decodePacketAscii(payload=binascii.unhexlify(binascii.hexlify(responder.tobytes()))))
                                    self.CTconnection.execute(_insert)
                                except Exception as e:
                                    self.showMessage("unable to insert data into database!",color='red',blink='y')
                                self.nextwInd = 1
                                break
                            except KeyboardInterrupt:
                                print("bmRequest=0x{0:02X}, bRequest=0x{1:02X},wValue=0x{2:04X} , wIndex=0x{3:02X}, data_length=0x{4:02X} *******************************\n".format(i,j,q,w,l))
                            except Exception as e:
                                #print(e)
                                pass
        try:
            self.CTtransaction.commit()
            self.CTconnection.close()
        except:
            pass
        self.showMessage("Ended!",color="green")

    def decodePacketAscii(self,payload=None):
        """
        This method decodes packet bytes back to Ascii
        :param payload: bytes of payload to be converted to ascii
        :return: decoded payload
        """
        retpayload = ""
        for i in payload:
            decode = chr(ord(chr(i)))
            if decode.isalnum():
                retpayload += decode
            else:
                retpayload += "."
        return retpayload

    def replaymsgs(self, direction=None, sequence=None, timeout=0.5):
        """This method searches the USBLyzer parsed database and give you the option replay a message or all messages from host to device
        :param direction: in or out
        :param sequence: the sequence number you would like to select to reply
        :param message: will allow you to send your selected message
        :param timeout: how long to wait between messages
        """
        count = 0
        if direction == 'in':
            self.startQueuewrite()
        try:
            if self.device:
                if sequence is None and direction is not None:
                    self.searchResults = self.connection.execute('select distinct RawBinary from "%s" where io="%s"'%(self.dbname,direction)).fetchall()
                    for i in self.searchResults:
                                count += 1
                                try:
                                    if direction == 'out':
                                        if self.fuzzdevice ==1:
                                            packet = memoryview(i[0]).tolist()
                                            random.shuffle(packet)
                                            packet = binascii.unhexlify(''.join(format(x, '02x') for x in packet))
                                            print(packet)
                                            self.device.write(self.epout, packet,self.device.bMaxPacketSize0)
                                        else:
                                            self.device.write(self.epout, i[0], self.device.bMaxPacketSize0)
                                            print(i[0])
                                        print("[%d]++++++++++^ TO DEVICE ^+++++++++++++"%count)
                                        sleep(timeout)
                                    if direction == 'in':
                                        if self.fuzzhost == 1:
                                            packet = memoryview(i[0]).tolist()
                                            random.shuffle(packet)
                                            packet = binascii.unhexlify(''.join(format(x, '02x') for x in packet))
                                            print(packet)
                                            self.hostwrite(packet)
                                        else:
                                            print(i[0])
                                            self.hostwrite(i[0])
                                        print("[%d] ++++++++++^ TO HOST ^+++++++++++++" % count)
                                        sleep(timeout)

                                except usb.core.USBError as e:
                                    print("[%d] ++++++++++ Comms Error +++++++++++++"%count)
                                    print(e)
                                    if e.args == ('Operation timed out',):
                                        print("timedout\n")
                                        continue
                                    print("[%d]++++++++++ Comms Error +++++++++++++"%count)
                elif sequence is not None and direction is not None:
                    count += 1
                    self.searchResults = self.connection.execute('select distinct RawBinary from "%s" where io="%s" and seq=%d' %(self.dbname, direction,sequence)).fetchone()
                    self.device.write(self.epout, self.searchResults[0], self.device.bMaxPacketSize0)
        except Exception as e:
            print("[-] Can't find messages with your search\n",e)


    def searchmsgs(self):
        """
        This method allows you to search and select all messages for a pattern which were saved from a USBlyzer database creation

        this method does not return anything
        """
        _cols = inspect(self.dbObj)
        _coldict = {}
        self._names= _cols.get_columns(self.dbname)
        print("id->Column")
        for i,j in enumerate(self._names):
            _coldict[i] = j['name']
        pprint.pprint(_coldict)
        self.colSelection = int(input("Search in which column id: "))
        self.searcher = input("Enter search text: ")
        self.searchResults = self.connection.execute('select distinct * from "%s" where %s like "%%%s%%"'\
                                                     %(self.dbname, _coldict[self.colSelection], self.searcher)).fetchall()
        self.searchdict = {}
        for i,j in enumerate(self.searchResults):
            self.searchdict[i] = j
        pprint.pprint(self.searchdict)
        self.msgSelected = self.searchdict[int(input("Which message id to select: "))]
        print (self.msgSelected)


    def usblyzerparse(self,dbname):
        """
        This method will parse your xml exported from usblyzer and then import them into a database

        :param dbname: this parameter is used to create a sqlite database in the folder ./databases with the specified name passed.

        this method returns nothing
        """
        try:
            self.dbname = "databases/"+dbname+"_"+self.SelectedDevice
            print("Creating Tables")
            self.dbObj,_table = self.createdb(self.dbname)
            self.connection = self.dbObj.connect()
            self.transaction = self.connection.begin()
            self.xmlfile = input("Enter  Path to USBlyzer xml dump: ")
            print("Parsing the file..")
            with open(self.xmlfile) as fd:
                self.xmlobj = xmltodict.parse(fd.read())
            print ("Inserting into database..")
            for i in self.xmlobj['USBlyzerXmlReport']['Items']['Item']:
                    try:
                        _type = i['Type']
                    except:
                        _type = ""
                    try:
                        _duration = i['Duration'].split(' ')[0]
                    except:
                        _duration = '0.0'
                    if "-" in i['Seq']:
                        _seq, _replyfrom  = map(int,i['Seq'].split("-"))
                    else:
                        _seq = int(i['Seq']) #seq
                        _replyfrom = 0
                    try:
                        _io = i['IO'] #IO
                    except:
                        _io = ""
                    try:
                        _cie = i['CIE'] #CIE
                    except:
                        _cie = ""
                    try:
                        _devObj = i['DevObjAddr'] #devobjaddr
                    except:
                        _devObj = ""
                    try:
                        _irpAddr= i['IrpAddr']  # irpaddr
                    except:
                        _irpAddr = ""
                    try:
                        _mSize = int(i['RawDataSize']) # raw size
                    except:
                        _mSize = 0
                    try:
                       _mData = ''.join(i['RawData'].split())
                       _mDataAscii = binascii.unhexlify(_mData)
                    except Exception as e:
                        _mData = ""
                        _mDataAscii = ""
                    try:
                            _insert = _table.insert().values(
                                Type = _type,
                                seq=_seq,
                                io=_io,
                                cie=_cie,
                                Duration=_duration,
                                DevObjAddr =_devObj,
                                irpaddr=_irpAddr,
                                RawDataSize = _mSize,
                                RawData =_mData,
                                RawBinary = _mDataAscii,
                                replyfrom =_replyfrom)
                            self.connection.execute(_insert)
                    except Exception as e:
                        self.showMessage("unable to insert data into database!\n",color='red',blink='y')
                        break
            self.transaction.commit()
        except Exception as e:
            self.showMessage("Unable to create or parse!\n",color='red',blink='y')

    def clonedev(self):
        """
        This method does not need any parameters it only saves a backup of the device incase you need to share it or use it later.
        saves the device information in the ./clones/ directory.

        The best option is to allow Agfs to claim the interfaces prior to cloning it as we need to gather more info on the device
        before we clone it.

        This method returns nothing.
        """
        try:
            try:
                self.device_hidrep
            except:
                self.showMessage("Claim the interfaces before trying to clone the device. We need some info",color='red')
                return "Cloning Failed"
            try:
                self.devcfg.bmAttributes
            except:
                self.showMessage("Claim the interfaces before trying to clone the device. We need some info",color='red')
                return "Cloning Failed"
            try:
                self.devcfg.bMaxPower
            except:
                self.showMessage("Claim the interfaces before trying to clone the device. We need some info",color='red')
                return "Cloning Failed"
            cloner = open("clones/%s" % self.SelectedDevice, 'w')
            print("setting up: %s" % self.manufacturer)
            print("Creating backup of device\n")
            self.devJson = json.dumps({"idVen":'0x{:04X}'.format(self.device.idVendor),\
                                  "idProd":'0x{:04X}'.format(self.device.idProduct),\
                                  "manufacturer":self.manufacturer,\
                                  "bcdDev":'0x{:04X}'.format(self.device.bcdDevice),\
                                  "bcdUSB":'0x{:04X}'.format(self.device.bcdUSB),\
                                  "serial":self.device.serial_number,\
                                  "bDevClass":'0x{:02X}'.format(self.device.bDeviceClass),\
                                  "bDevSubClass":'0x{:02X}'.format(self.device.bDeviceSubClass),\
                                  "protocol":'0x{:02X}'.format(self.device.bDeviceProtocol),\
                                  "MaxPacketSize":'0x{:02X}'.format(self.device.bMaxPacketSize0),\
                                  "hidreport":','.join([i.decode('utf-8') for i in self.device_hidrep]),\
                                  "bmAttributes":'0x{:02X}'.format(self.devcfg.bmAttributes),\
                                  "MaxPower":'0x{:02X}'.format(self.devcfg.bMaxPower),
                                  "product":self.device.product})
            cloner.write(self.devJson)
            cloner.write('\n++++++\n')
            cloner.write(str(self.device)+"\n\n")
            print("- Done: Device settings copied to file.\n")
            cloner.close()
        except Exception as e:
            self.showMessage("Cannot clone the device!\n", color='red',blink='y')

    def setupGadgetFS(self):
        """ setup variables for gadgetFS : Linux Only, on Raspberry Pi Zero best option
        This method does not require any parameters.
        calling this method creates a bash script file inside the directory ./gadgetscripts/ which can then be pushed
        and executed on the pi Zero to emulate the device being tested.

        This method returns nothing.
        """
        try:
            agfsscr = open("gadgetscripts/"+self.SelectedDevice+".sh",'w')
            print("setting up: "+self.manufacturer)
            print("Aquiring info about the device for Gadetfs\n")
            idVen = '0x{:04X}'.format(self.device.idVendor)
            idProd = '0x{:04X}'.format(self.device.idProduct)
            manufacturer = self.manufacturer
            bcdDev = '0x{:04X}'.format(self.device.bcdDevice)
            bcdUSB = '0x{:04X}'.format(self.device.bcdUSB)
            serial = self.device.serial_number
            """http://irq5.io/2016/12/22/raspberry-pi-zero-as-multiple-usb-gadgets/"""
            windows = input("are you going to configure this gadget to work with windows [y/n] ?").lower()
            if windows == 'y':
                bDevClass = '0x{:02X}'.format(0xEF)
                bDevSubClass = '0x{:02X}'.format(0x02)
                protocol = '0x{:02X}'.format(0x01)
            else:
                bDevClass = '0x{:02X}'.format(self.device.bDeviceClass)
                bDevSubClass = '0x{:02X}'.format(self.device.bDeviceSubClass)
                protocol = '0x{:02X}'.format(self.device.bDeviceProtocol)
            MaxPacketSize = '0x{:04X}'.format(self.device.bMaxPacketSize0)
            if len(self.device_hidrep) != 0:
                for i,j in enumerate(self.device_hidrep):
                    print(i,"] ",j)
                hidq = int(input("Which report would you like to use? "))
                hidreport = self.device_hidrep[hidq]
            else:
                hidreport=''.encode('utf-8')
            bmAttributes = '0x{:02X}'.format(self.devcfg.bmAttributes)
            MaxPower = '0x{:02X}'.format(self.devcfg.bMaxPower)
            product = self.device.product
            basedir = "/sys/kernel/config/usb_gadget"
            agfsscr.write("#!/bin/bash\n")
            agfsscr.write("rmmod g_serial\n")
            agfsscr.write("modprobe libcomposite\n")
            agfsscr.write("cd /sys/kernel/config/usb_gadget/\n")
            agfsscr.write("mkdir g && cd g\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/strings/0x409/\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/functions/hid.usb0/\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/\n")
            agfsscr.write("echo %s > %s/g/idVendor\n"%(idVen,basedir))
            agfsscr.write("echo %s > %s/g/idProduct\n" % (idProd, basedir))
            agfsscr.write("echo %s > %s/g/bcdDevice\n" % (bcdDev, basedir))
            agfsscr.write("echo %s > %s/g/bcdUSB\n" % (bcdUSB, basedir))
            agfsscr.write("echo %s > %s/g/bDeviceClass\n" % (bDevClass, basedir))
            agfsscr.write("echo %s > %s/g/bDeviceSubClass\n" % (bDevSubClass, basedir))
            agfsscr.write("echo %s > %s/g/bDeviceProtocol\n" % (protocol, basedir))
            agfsscr.write("echo %s > %s/g/bMaxPacketSize0\n" % (MaxPacketSize, basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/serialnumber\n" % (serial, basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/manufacturer\n" % (manufacturer, basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/product\n" % (product, basedir))
            agfsscr.write("echo %s > %s/g/configs/c.1/MaxPower\n" % (MaxPower, basedir))
            agfsscr.write("echo %s > %s/g/configs/c.1/bmAttributes\n" % (bmAttributes, basedir))
            agfsscr.write("echo 'Default Configuration' > %s/g/configs/c.1/strings/0x409/configuration\n" %(basedir))
            agfsscr.write("echo %s > %s/g/functions/hid.usb0/protocol\n" %(protocol,basedir))
            agfsscr.write("echo 256 > %s/g/functions/hid.usb0/report_length\n" %(basedir))
            agfsscr.write("echo %s > %s/g/functions/hid.usb0/subclass\n" % (bDevSubClass,basedir))
            agfsscr.write("echo '%s' | xxd -r -ps > %s/g/functions/hid.usb0/report_desc\n" % (hidreport.decode("utf-8") ,basedir))
            agfsscr.write("ln -s %s/g/functions/hid.usb0 %s/g/configs/c.1\n"%(basedir,basedir))
            agfsscr.write("udevadm settle -t 5 || :\n")
            agfsscr.write("ls /sys/class/udc/ > %s/g/UDC\n"%(basedir))
            agfsscr.close()
            push2pi = input("Do you want to push the gadget to the Pi zero ?[y/n] ").lower()
            if push2pi == 'y':
                '''https://stackoverflow.com/questions/3635131/paramikos-sshclient-with-sftps'''
                self.pihost = input("Enter the ip address of the Pi zero: ")
                self.piport = int(input("Enter the port of the Pi zero: "))
                self.piuser = input("Enter the username: ")
                self.pipass = getpass.getpass()
                print("Connecting...")
                pusher = paramiko.Transport((self.pihost,self.piport))
                pusher.connect(None, self.piuser, self.pipass)
                sftp = paramiko.SFTPClient.from_transport(pusher)
                print("Sending...")
                sftp.put(f"gadgetscripts/{self.SelectedDevice}.sh",f"gadgets/{self.SelectedDevice}.sh")
                print("Done!")
                if sftp:
                    sftp.close()
                if pusher:
                    pusher.close()
                rungadget = input("Do you want to run the gadget? [y/n]").lower()
                if rungadget == 'y':
                    gogadget = paramiko.SSHClient()
                    gogadget.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    gogadget.connect(self.pihost, port=self.piport, username=self.piuser, password=self.pipass)
                    stdin, stdout, stderr = gogadget.exec_command(f"chmod a+x gadgets/{self.SelectedDevice}.sh;sudo gadgets/{self.SelectedDevice}.sh")
                    self.showMessage("Gadget should now be running",color='blue')

        except Exception as e:
            self.showMessage("You need to call FindSelect() then clonedev() method method prior to setting up GadgetFS", color='red',blink='y')

    def removeGadget(self):
        """
        This method removes the gadget from the raspberryPI
        :return: None
        """
        try:
            remgadget = paramiko.SSHClient()
            remgadget.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            remgadget.connect(self.pihost, port=self.piport, username=self.piuser, password=self.pipass)
            stdin, stdout, stderr = remgadget.exec_command('sudo ./removegadget.sh')
            self.showMessage("Gadgets are removed", color='blue', blink='y')
        except:
            self.showMessage("No gadgets are setup! Nothing to do.",color='red',blink='y')

    def showMessage(self,string,color='green',blink=None):
        """shows messages if error or warn or info"""
        cprint(f"{'*'*(len(string)+4)}\n{string}\n{'*'*(len(string)+4)}",color, attrs=[] if blink is None else ['blink'])

    def help(self, method, source=None):
        """
        AutogadgetFS Help method
        :param method: takes in a method name and gives you the method signature and its doc strings
        :param source: option to view the source of the current method passed to help
        :return: None
        """
        try:
            target = f"agfs.{method}"
            cprint(f"****\n[+]Help for {eval(target).__name__} Method:", color="white")
            cprint(f"[-]Signature: {eval(target).__name__}{inspect.signature(eval(target))}\n", color="blue")
            cprint(f"\n[+]{eval(target).__name__} Help:", color="white")
            cprint(f"{inspect.getdoc(eval(target))}", color="blue")
            if source != None:
                cprint(f"\n[+]Source code of method {eval(target).__name__}:", color="white")
                cprint(f"{inspect.getsource(eval(target))}", color="green")
            cprint("****", color="white")
        except:
            method_list = [meth for meth in dir(agfs) if callable(getattr(agfs, meth)) and not meth.startswith("__")]
            method_list.sort()
            cprint("Currently supported methods:" ,color='white')
            max_length = 28
            alt = ['green','blue']
            c = 0
            for item in method_list:
                cprint('{0:>{1}}'.format(item, max_length) ,color=alt[c]),
                c += 1
                if c > 1:
                    c = 0
