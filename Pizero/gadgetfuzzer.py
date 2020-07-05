import argparse
from time import sleep
from os import urandom,system,write
import shlex
import binascii
from random import randint,choice


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-v',dest='vendor',help='Vendor ID', required=False,default=None)
    argparse.add_argument('-p',dest='product',help='Product ID', required=False,default=None)
    argparse.add_argument('-c',dest='dclass',help='device class', required=False,default=None)
    argparse.add_argument('-man',dest='man',help='device class', required=False,default=None)
    argparse.add_argument('-prod',dest='prod',help='device class', required=False,default=None)
    argparse.add_argument('-t',dest='timeout',help='Timeout',type=int, required=False,default=1)
    argparse.add_argument('-s',dest='samples',help='Samples to generate', type=int, required=True,default=100)
    argparse.add_argument('-min',dest='min',help='max length of report', required=False,default=0)
    argparse.add_argument('-max',dest='max',help='max length of report', required=False,default=10)
    argparse.add_argument('-i',dest='serial',help='custom serial number of device', required=False,default="AutoGadgetFS")
    args = argparse.parse_args()
    chmodgadget = "chmod a+x tempgadget.sh"
    removegadget = "./removegadget.sh"
    creategadget ="./tempgadget.sh"
    for i in range(args.samples):
        print(f"Generation: [{i}]")
        with open('tempgadget.sh','w') as agfsscr:
            basedir = "/sys/kernel/config/usb_gadget"
            agfsscr.write("#!/bin/bash\n")
            #agfsscr.write("rmmod g_serial\n")
            agfsscr.write("modprobe libcomposite\n")
            agfsscr.write("cd /sys/kernel/config/usb_gadget/\n")
            agfsscr.write("mkdir g && cd g\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/strings/0x409/\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/functions/hid.usb0/\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/\n")
            agfsscr.write("echo %s > %s/g/idVendor\n" % (args.vendor if args.vendor else f"0x{binascii.hexlify(urandom(2)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/idProduct\n" % (args.product if args.product else f"0x{binascii.hexlify(urandom(2)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bcdDevice\n" % ("0x200", basedir))
            agfsscr.write("echo %s > %s/g/bcdUSB\n" % ("0x0058", basedir))
            agfsscr.write("echo %s > %s/g/bDeviceClass\n" % (args.dclass if args.dclass else f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bDeviceSubClass\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bDeviceProtocol\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bMaxPacketSize0\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/strings/0x409/serialnumber\n" % (args.serial if args.serial else f"{binascii.hexlify(urandom(50))}%c%c%c%s%s%s%d%p", basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/manufacturer\n" % (args.man if args.man else f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/product\n" % (args.prod if args.prod else f"0x{binascii.hexlify(urandom(50)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/configs/c.1/MaxPower\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/configs/c.1/bmAttributes\n" % ("0x80", basedir))
            agfsscr.write("echo 'Default Configuration' > %s/g/configs/c.1/strings/0x409/configuration\n" % (basedir))
            agfsscr.write("echo %s > %s/g/functions/hid.usb0/protocol\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo 256 > %s/g/functions/hid.usb0/report_length\n" % (basedir))
            agfsscr.write("echo %s > %s/g/functions/hid.usb0/subclass\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
           # s = choice(["c0c0c0c0c0c0c0c0",f"05010900a1{binascii.hexlify(urandom(randint(int(args.min),int(args.max)))).decode()}c0",f"{binascii.hexlify(urandom(randint(int(args.min),int(args.max)))).decode()}c0c0c0c0c0c0c0"])
            s = f"05010900a1{binascii.hexlify(urandom(randint(int(args.min),int(args.max)))).decode()}c0"
            #s = "05010900a101150026ff0019002900750895408102190029009102c0"
            #print(len(s))
            agfsscr.write("echo '%s' | xxd -r -ps > %s/g/functions/hid.usb0/report_desc\n" % (s, basedir))
            agfsscr.write("ln -s %s/g/functions/hid.usb0 %s/g/configs/c.1\n" % (basedir, basedir))
            agfsscr.write("udevadm settle -t 5 || :\n")
            agfsscr.write("ls /sys/class/udc/ > %s/g/UDC\n" % (basedir))
            agfsscr.close()
        system(chmodgadget)
        system(creategadget)
        sleep(args.timeout)
        #writepacket = open("/dev/hidg0",'wb')
        #s = urandom(randint(0,64))
        #print(s)
        #write(writepacket.fileno(),s)
        sleep(int(args.timeout))
        system(removegadget)


