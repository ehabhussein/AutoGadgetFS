#!/usr/bin/python3
#Ehab Hussein
##################### Imports
import xmltodict
import platform
import binascii
from sys import exit
from os import geteuid, system, mkdir
from sqlalchemy import MetaData, create_engine, String, Integer, Table, Column, inspect
import pprint
######################Thanks To

#Josep Rodriguez for the Inspiration

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
    import usb.core
    import usb.util
except:
    print ("Seems like you done have pyusb installed.\n[-]install it via pip:\n\t[-]pip3 install pyusb")
    exit(-1)

############auto gadgetFS class

class afs():
    def __init__(self):
        print ("""
       *******************************************************************************
       *AutoGadgetFS: Automated USB testing based on gadgetfs*************************
       *******************************************************************************     
        """)

    def createdb(self, name):
        '''create the sqlite table and columns for usblyzer dumps'''
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
            Column('RawAscii',String),
            Column('replyfrom', Integer)
                                    )
            meta.create_all(db)
            return db, self.usblyzerdb
        except:
            print("[Error] cannot create db\n")

    def releasedev(self):
        '''releases the device and re-attaches the kernel driver'''
        print("[-] Releasing the Interface")
        usb.util.release_interface(self.device, self.interfaces.bInterfaceNumber)
        print("[-] Attaching the kernel driver")
        self.device.attach_kernel_driver(self.interfaces.bInterfaceNumber)
        print("[-] Device released!")

    def deviceInfo(self):
        '''gets the complete info only for any usb connected to the host'''
        getusbs = usb.core.find(find_all=True)
        devices = dict(enumerate(str(dev.manufacturer) + ":" + str(dev.idProduct) + ":" + str(dev.idVendor) for dev in getusbs))
        for key, value in devices.items():
            print(key, ":", value)
        hook = input("---> Select a device: ")
        idProd, idVen = devices[int(hook)].split(':')[1:]
        device = usb.core.find(idVendor=int(idVen), idProduct=int(idProd))
        print(device)

    def deviceInterfaces(self):
        '''get all interfaces and endpoints on the device'''
        for cfg in self.device:
            print("Configuration Value: "+str(int(cfg.bConfigurationValue)) + '\n')
            for intf in cfg:
                print('\tInterface number: ' + \
                                 str(int(intf.bInterfaceNumber)) + \
                                 ',Alternate Setting: ' + \
                                 str(intf.bAlternateSetting) + \
                                 '\n')
                for ep in intf:
                    print('\t\tEndpoint Address: ' + \
                                     hex(ep.bEndpointAddress) + \
                                     '\n')
    def changeintf(self):
        '''will allow you to change the interfaces you use with the device '''
        self.deviceInterfaces()
        self.precfg = int(input("which Configuration would you like to use: "))
        self.interfacenumber = int(input("which Interface would you like to use: "))
        self.Alternate = int(input("which Alternate setting would you like to use: "))
        self.epin = int(input("which Endpoint IN would you like to use: "), 16)
        self.epout = int(input("which Endpoint OUT would you like to use: "), 16)
        self.interfaces = self.devcfg[(self.interfacenumber, self.Alternate)]


    def findSelect(self):
        '''find your device and select it'''
        self.getusbs = usb.core.find(find_all=True)
        self.devices = dict(enumerate(str(dev.manufacturer)+":"+str(dev.idProduct)+":"+str(dev.idVendor) for dev in self.getusbs))
        for key,value in self.devices.items():
            print(key,":",value)
        self.hook = input("---> Select a device: ")
        self.idProd,self.idVen = self.devices[int(self.hook)].split(':')[1:]
        self.device = usb.core.find(idVendor=int(self.idVen),idProduct=int(self.idProd))
        print(str(self.device))
        detachKernel = str(input("do you want to detach the device from it's kernel driver: [y/n] "))
        if detachKernel.lower() == 'y':
            self.deviceInterfaces()
            try:
                try:
                    self.device.set_configuration()
                except Exception as e:
                    print("Can't set device configuration. not a problem!")
                self.devcfg = self.device.get_active_configuration()
                self.changeintf()
            except Exception as e:
                print(e)
                print("Couldn't get device configuration!")
            if self.device.is_kernel_driver_active(self.interfaces.bInterfaceNumber):
                self.device.detach_kernel_driver(self.interfaces.bInterfaceNumber)
                print("[-] Kernel driver detached")
            claim = str(input("Do you want pyUSB to claim the device interface: [y/n] "))
            if claim.lower() == 'y':
                    usb.util.claim_interface(self.device, self.interfaces.bInterfaceNumber)
                    print("Checking HID report retrieval\n")
                    try:
                        self.device_hidrep = binascii.hexlify(self.device.ctrl_transfer(self.epin,6,0x2200,self.interfaces.bInterfaceNumber,0x400))
                        if self.device_hidrep:
                            print(self.device_hidrep.decode("utf-8"))
                            print("Success, now you can use the setupGadgetFS() method to use the device with GadgetFS\n")
                    except:
                        print("Couldn't get a hid report but we have claimed the device.")

    def sniffdevice(self, howmany, endpoint):
        ''' man in the middle the communication between the device and host
         This is mostly taken from https://www.orangecoat.com/how-to/read-and-decode-data-from-your-mouse-using-this-pyusb-hack '''
        if endpoint == 'in':
            endpoint = self.epin
        else:
            endpoint = self.epout
        collected = 0
        attempts = int(howmany)
        while collected < attempts:
            try:
                data = self.device.read(endpoint, self.device.bMaxPacketSize0)
                collected += 1
                print(data)
            except usb.core.USBError as e:
                data = None
                if e.args == ('Operation timed out',):
                    continue

    def replaymsgs(self, direction=None, sequence=None , message=None):
        '''replay a message from host to device'''
        try:
            if self.device:
                if sequence is None and direction is not None and message is None:
                    self.searchResults = self.connection.execute('select RawData from "%s" where io="%s"'%(self.dbname,direction)).fetchall()
                    for i in self.searchResults:
                        pprint.pprint(i[0])
                elif sequence is not None and direction is not None and message is None:
                    self.searchResults = self.connection.execute('select RawData from "%s" where io="%s" and seq=%d' %(self.dbname, direction,sequence)).fetchall()
                    pprint.pprint(self.searchResults[0][0])
                elif message is not None:
                    print("[-] Sending your custom message.")
                else:
                    pass
        except Exception as e:
            print("[-] Can't find messages with your search\n",e)


    def searchmsgs(self):
        '''search and select all messages for a pattern'''
        _cols = inspect(self.dbObj)
        _coldict = {}
        self._names= _cols.get_columns(self.dbname)
        print("id->Column")
        for i,j in enumerate(self._names):
            _coldict[i] = j['name']
        pprint.pprint(_coldict)
        self.colSelection = int(input("Search in which column id: "))
        self.searcher = input("Enter search text: ")
        self.searchResults = self.connection.execute('select * from "%s" where %s like "%%%s%%"'\
                                                     %(self.dbname, _coldict[self.colSelection], self.searcher)).fetchall()
        self.searchdict = {}
        for i,j in enumerate(self.searchResults):
            self.searchdict[i] = j
        pprint.pprint(self.searchdict)
        self.msgSelected = self.searchdict[int(input("Which message id to select: "))]
        print (self.msgSelected)


    def usblyzerparse(self,dbname):
        '''This method with parse your xml exported from usblyzer and then import them into the database'''
        try:
            self.dbname = dbname
            print("Creating Tables")
            self.dbObj,_table = self.createdb(self.dbname)
            self.connection = self.dbObj.connect()
            self.transaction = self.connection.begin()
            self.xmlfile = input("Enter Path to USBlyzer xml dump: ")
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
                                RawAscii = _mDataAscii,
                                replyfrom =_replyfrom)
                            self.connection.execute(_insert)
                    except Exception as e:
                        print("unable to insert data into database!",e)
                        break
            self.transaction.commit()
        except Exception as e:
            print("Unable to create or parse!",e)

    def listengadgetfs(self):
        '''will emulate a device and send responses back to the host'''
        pass

    def setupGadgetFS(self):
        ''' setup variables for gadgetFS : Linux Only'''
        try:
            print("setting up: "+self.device.manufacturer)
            print("Aquiring info about the device for Gadetfs\n")
            idVen = '0x{:04X}'.format(self.device.idVendor)
            idProd = '0x{:04X}'.format(self.device.idProduct)
            manufacturer = self.device.manufacturer
            bcdDev = '0x{:04X}'.format(self.device.bcdDevice)
            bcdUSB = '0x{:04X}'.format(self.device.bcdUSB)
            serial = ''
            bDevClass = '0x{:04X}'.format(self.device.bDeviceClass)
            bDevSubClass = hex(self.device.bDeviceSubClass)
            protocol = hex(self.device.bDeviceProtocol)
            MaxPacketSize = '0x{:04X}'.format(self.device.bMaxPacketSize0)
            hidreport = self.device_hidrep.decode("utf-8")
            bmAttributes = hex(self.devcfg.bmAttributes)
            MaxPower = hex(self.devcfg.bMaxPower)
            product = self.device.product
            print("- Done: Device settings copied.\n")
            doCfgGFs = input("Shall we configure the system? [y/n] ")
            if doCfgGFs.lower() == 'y':
                basedir ="cfg/"
                print("removing g_serial\n")
                system("rmmod g_serial")
                print("Adding libcomposite\n")
                system("modprobe libcomposite")
                print("Setting up Gadgetfs\n")
                mkdir("%s"%basedir)
                system("mount none cfg -t configfs")
                system("echo %s > %s/g/idVendor"%(idVen,basedir))
                system("echo %s > %s/g/idProduct" % (idProd, basedir))
                system("echo %s > %s/g/bcdDevice" % (bcdDev, basedir))
                system("echo %s > %s/g/bcdUSB" % (bcdUSB, basedir))
                system("echo %s > %s/g/bDeviceClass" % (bDevClass, basedir))
                system("echo %s > %s/g/bDeviceSubClass" % (bDevSubClass, basedir))
                system("echo %s > %s/g/bDeviceProtocol" % (protocol, basedir))
                system("echo %s > %s/g/bMaxPacketSize0" % (MaxPacketSize, basedir))

                pathlib.Path('%s/g/strings/0x409/').mkdir(parents=True, exist_ok=True)
                system("echo %s > %s/g/strings/0x409/serialnumber" % (serial, basedir))
                system("echo %s > %s/g/strings/0x409/manufacturer" % (manufacturer, basedir))
                system("echo %s > %s/g/strings/0x409/product" % (product, basedir))

                pathlib.Path('%s/g/configs/c.1/strings/0x409/').mkdir(parents=True, exist_ok=True)
                system("echo %s > %s/g/configs/c.1/MaxPower" % (MaxPower, basedir))
                system("echo %s > %s/g/configs/c.1/bmAttributes" % (bmAttributes, basedir))
                system("echo 'Default Configuration' > %s/g/configs/c.1/strings/0x409/configuration" %(basedir))

                pathlib.Path('%s/g/functions/hid.usb0/').mkdir(parents=True, exist_ok=True)
                system("echo 0 > %s/g/functions/hid.usb0/protocol" %(basedir))
                system("echo 64 > %s/g/functions/hid.usb0/report_length" % (basedir))
                system("echo 0 > %s/g/functions/hid.usb0/subclass" % (basedir))
                system("echo %s | xxd -r -ps > %s/g/functions/hid.usb0/report_desc" % (str(hidreport),basedir))
                system("ln -s %s/g/functions/hid.usb0 %s/g/configs/c.1"%(basedir,basedir))
                system("udevadm settle -t 5 || :")
                system("ls /sys/class/udc/ > %s/g/UDC"%(basedir))
            print("- Done. Try testing your gadget\n")

        except Exception as e:
            print("You need to call FindSelect() then clone() method method prior to setting up GadgetFS",e)
