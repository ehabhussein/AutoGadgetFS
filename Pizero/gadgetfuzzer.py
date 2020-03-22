import argparse
from time import sleep
from os import urandom,system
import shlex
import binascii
from random import randint

if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument('-v',dest='vendor',help='Vendor ID', required=False,default=None)
    argparse.add_argument('-p',dest='product',help='Product ID', required=False,default=None)
    argparse.add_argument('-c',dest='dclass',help='device class', required=False,default=None)
    argparse.add_argument('-t',dest='timeout',help='Timeout', required=False,default=1)
    argparse.add_argument('-s',dest='samples',help='Samples to generate', type=int, required=True,default=100)
    args = argparse.parse_args()
    chmodgadget = "chmod a+x tempgadget.sh"
    removegadget = "./removegadget.sh"
    creategadget ="./tempgadget.sh"
    system("rmmod g_serial")
    for i in range(args.samples):
        print(f"Generation: [{i}]")
        with open('tempgadget.sh','w') as agfsscr:
            basedir = "/sys/kernel/config/usb_gadget"
            agfsscr.write("#!/bin/bash\n")
            agfsscr.write("modprobe libcomposite\n")
            agfsscr.write("cd /sys/kernel/config/usb_gadget/\n")
            agfsscr.write("mkdir g && cd g\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/strings/0x409/\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/functions/hid.usb0/\n")
            agfsscr.write("mkdir -p /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/\n")
            agfsscr.write("echo %s > %s/g/idVendor\n" % (args.vendor if args.vendor else f"0x{binascii.hexlify(urandom(2)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/idProduct\n" % (args.product if args.product else f"0x{binascii.hexlify(urandom(2)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bcdDevice\n" % ("0x3", basedir))
            agfsscr.write("echo %s > %s/g/bcdUSB\n" % ("0x0058", basedir))
            agfsscr.write("echo %s > %s/g/bDeviceClass\n" % (args.dclass if args.dclass else f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bDeviceSubClass\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bDeviceProtocol\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/bMaxPacketSize0\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/serialnumber\n" % (f"0x{binascii.hexlify(urandom(10)).decode()}", basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/manufacturer\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo '%s' > %s/g/strings/0x409/product\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/configs/c.1/MaxPower\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo %s > %s/g/configs/c.1/bmAttributes\n" % ("0x80", basedir))
            agfsscr.write("echo 'Default Configuration' > %s/g/configs/c.1/strings/0x409/configuration\n" % (basedir))
            agfsscr.write("echo %s > %s/g/functions/hid.usb0/protocol\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            agfsscr.write("echo 256 > %s/g/functions/hid.usb0/report_length\n" % (basedir))
            agfsscr.write("echo %s > %s/g/functions/hid.usb0/subclass\n" % (f"0x{binascii.hexlify(urandom(1)).decode()}", basedir))
            s = f"05010900a1{binascii.hexlify(urandom(randint(0,23))).decode()}c0"
            agfsscr.write("echo '%s' | xxd -r -ps > %s/g/functions/hid.usb0/report_desc\n" % (s, basedir))
            agfsscr.write("ln -s %s/g/functions/hid.usb0 %s/g/configs/c.1\n" % (basedir, basedir))
            agfsscr.write("udevadm settle -t 5 || :\n")
            agfsscr.write("ls /sys/class/udc/ > %s/g/UDC\n" % (basedir))
            agfsscr.close()
        system(chmodgadget)
        system(creategadget)
        sleep(int(args.timeout))
        system(removegadget)


