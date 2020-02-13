#!/bin/bash
rmmod g_serial
modprobe libcomposite
cd /sys/kernel/config/usb_gadget/
mkdir g && cd g
mkdir -p /sys/kernel/config/usb_gadget/g/strings/0x409/
mkdir -p /sys/kernel/config/usb_gadget/g/functions/hid.usb0/
mkdir -p /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/
echo 0x258A > /sys/kernel/config/usb_gadget/g/idVendor
echo 0x1006 > /sys/kernel/config/usb_gadget/g/idProduct
echo 0x0100 > /sys/kernel/config/usb_gadget/g/bcdDevice
echo 0x0110 > /sys/kernel/config/usb_gadget/g/bcdUSB
echo 0xEF > /sys/kernel/config/usb_gadget/g/bDeviceClass
echo 0x02 > /sys/kernel/config/usb_gadget/g/bDeviceSubClass
echo 0x01 > /sys/kernel/config/usb_gadget/g/bDeviceProtocol
echo 0x0008 > /sys/kernel/config/usb_gadget/g/bMaxPacketSize0
echo 'None' > /sys/kernel/config/usb_gadget/g/strings/0x409/serialnumber
echo 'SINO WEALTH' > /sys/kernel/config/usb_gadget/g/strings/0x409/manufacturer
echo 'USB KEYBOARD' > /sys/kernel/config/usb_gadget/g/strings/0x409/product
echo 0x32 > /sys/kernel/config/usb_gadget/g/configs/c.1/MaxPower
echo 0xA0 > /sys/kernel/config/usb_gadget/g/configs/c.1/bmAttributes
echo 'Default Configuration' > /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/configuration
echo 0x01 > /sys/kernel/config/usb_gadget/g/functions/hid.usb0/protocol
echo 256 > %s/g/functions/hid.usb0/report_length
echo 0x02 > /sys/kernel/config/usb_gadget/g/functions/hid.usb0/subclass
echo '05010906a101050719e029e71500250175019508810295017508810195037501050819012903910295057501910195067508150026ff00050719002aff008100c0' | xxd -r -ps > /sys/kernel/config/usb_gadget/g/functions/hid.usb0/report_desc
ln -s /sys/kernel/config/usb_gadget/g/functions/hid.usb0 /sys/kernel/config/usb_gadget/g/configs/c.1
udevadm settle -t 5 || :
ls /sys/class/udc/ > /sys/kernel/config/usb_gadget/g/UDC
