#!/bin/bash
cd /sys/kernel/config/usb_gadget/g
echo "" > UDC
rm configs/c.1/hid.usb0
rmdir configs/c.1/strings/0x409
rmdir configs/c.1
rmdir strings/0x409
rmdir functions/hid.usb0
cd ..
rmdir g
