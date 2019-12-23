<pre>
# AutoGadgetFS
Usb testing framework

Work In progress. will be documented when the project is launched. No sending and receiving yet.


****************************************************************************************************************************

foo@Wakanda:/home/raindrop/PycharmProjects/AutoGadgetFs# ipython
Python 3.7.5 (default, Oct 27 2019, 15:43:29) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.9.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import libagfs                                                                                                                                                                        

In [2]: x = libagfs.afs()                                                                                                                                                                     

       *******************************************************************************
       *AutoGadgetFS: Automated USB testing based on gadgetfs*************************
       *******************************************************************************     
        

In [5]: x.findSelect()                                                          
0 : VIA Labs, Inc.:2071:8457
1 : Linux 5.3.0-kali2-amd64 xhci-hcd:3:7531
2 : Linux 5.3.0-kali2-amd64 xhci-hcd:2:7531
3 : Linux 5.3.0-kali2-amd64 xhci-hcd:3:7531
4 : Logitech:50475:1133
5 : VIA Technologies Inc.         :258:8457
6 : SINO WEALTH:4102:9610
7 : VIA Labs, Inc.:10263:8457
8 : None:57506:1161
9 : CN09357GLOG008CLA8P2A01:26403:3141
10 : NUVOTON:41750:1046
11 : Linux 5.3.0-kali2-amd64 xhci-hcd:2:7531
---> Select a device: 10
DEVICE ID 0416:a316 on Bus 001 Address 038 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x110 USB 1.1
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0x0416
 idProduct              : 0xa316
 bcdDevice              :    0x0 Device 0.0
 iManufacturer          :    0x1 NUVOTON
 iProduct               :    0x2 WPM USB
 iSerialNumber          :    0x0 
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 100 mA ==================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x29 (41 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0xc0 Self Powered
   bMaxPower            :   0x32 (100 mA)
    INTERFACE 1: Human Interface Device ====================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x1
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :    0x3 Human Interface Device
     bInterfaceSubClass :    0x0
     bInterfaceProtocol :    0x0
     iInterface         :    0x0 
      ENDPOINT 0x81: Interrupt IN ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x2
      ENDPOINT 0x2: Interrupt OUT ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x2 OUT
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x1
do you want to detach the device from it's kernel driver: [y/n] y
Disabling Interfaces on configuration: 1
Disabling interfaces :
	1
[-] Kernel driver detached
Configuration Value: 1

	Interface number: 1,Alternate Setting: 0

		Endpoint Address: 0x81

		Endpoint Address: 0x2

Do you want to reset the device? [y/n]: n
which Configuration would you like to use: 1
which Interface would you like to use: 0
which Alternate setting would you like to use: 0
which Endpoint IN would you like to use: 0x81
which Endpoint OUT would you like to use: 0x2
Do you want pyUSB to claim the device interface: [y/n] y
Checking HID report retrieval

1
[b'05010900a101150025ff190029ff954075088102190029ff9102c0']
[b'05010900a101150025ff190029ff954075088102190029ff9102c0']
Do you want to save this device's information?[y/n]y
setting up: NUVOTON
Creating backup of device

- Done: Device settings copied to file.


In [6]: x.setupGadgetFS()                                                       
setting up: NUVOTON
Aquiring info about the device for Gadetfs

0 ]  b'05010900a101150025ff190029ff954075088102190029ff9102c0'
Which report would you like to use? 0
- Creating Bash script!

- Done wrote bash script. Try testing your gadget
In [7]: x.startSniffReadThread(100,x.epin)                                                                                                                                                    

-----------------vvvFROM DEVICEvvv----------------
array('B', [1, 1, 1, 85, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
-----------------^^^FROM DEVICE^^^----------------                                                      

In [8]: x.device.write(x.epout,array.array('B', [1, 1,1, 1, 0, 0, 0, 0, 0]))                                                                                                                  
Out[8]: -----------------vvvFROM DEVICEvvv----------------
9
array('B', [1, 1, 1, 85, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
-----------------^^^FROM DEVICE^^^----------------

In [9]: x.device.write(x.epout,array.array('B', [1, 1,1, 1, 0, 0, 0, 0, 0]))                                                                                                                  
-----------------vvvFROM DEVICEvvv----------------
Out[9]: array('B', [1, 1, 1, 85, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
9
-----------------^^^FROM DEVICE^^^----------------

[10]: x.stopSniffing()                                                                                                                                                                     
Sniffing has stopped successfully!
In [11]: exit                                                                                                                                                                                  
foo@Wakanda:/home/raindrop/PycharmProjects/AutoGadgetFs# cat clones/NUVOTON-1046-41750-1575736170.7539692 
idVen=0x0416
idProd=0xA316
manufacturer=NUVOTON
bcdDev=0x0000
bcdUSB=0x0110
serial=0
bDevClass=0x0000
bDevSubClass=0x0
protocol=0x0
MaxPacketSize=0x0040
hidreport=[b'05010900a101150025ff190029ff954075088102190029ff9102c0']
bmAttributes=0xc0
MaxPower=0x32
product=WPM USB
++++++
DEVICE ID 0416:a316 on Bus 001 Address 059 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x110 USB 1.1
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :   0x40 (64 bytes)
 idVendor               : 0x0416
 idProduct              : 0xa316
 bcdDevice              :    0x0 Device 0.0
 iManufacturer          :    0x1 NUVOTON
 iProduct               :    0x2 WPM USB
 iSerialNumber          :    0x0 
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 100 mA ==================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x29 (41 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0xc0 Self Powered
   bMaxPower            :   0x32 (100 mA)
    INTERFACE 1: Human Interface Device ====================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x1
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :    0x3 Human Interface Device
     bInterfaceSubClass :    0x0
     bInterfaceProtocol :    0x0
     iInterface         :    0x0 
      ENDPOINT 0x81: Interrupt IN ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x2
      ENDPOINT 0x2: Interrupt OUT ==========================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x2 OUT
       bmAttributes     :    0x3 Interrupt
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x1

# cat NUVOTON-1046-41750-1577117694.9073.sh
#!/bin/bash
rmmod g_serial
modprobe libcomposite
cd /sys/kernel/config/usb_gadget/
mkdir g && cd g
mkdir -p /sys/kernel/config/usb_gadget/g/strings/0x409/
mkdir -p /sys/kernel/config/usb_gadget/g/functions/hid.usb0/
mkdir -p /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/
echo 0x0416 > /sys/kernel/config/usb_gadget/g/idVendor
echo 0xA316 > /sys/kernel/config/usb_gadget/g/idProduct
echo 0x0000 > /sys/kernel/config/usb_gadget/g/bcdDevice
echo 0x0110 > /sys/kernel/config/usb_gadget/g/bcdUSB
echo 0x00 > /sys/kernel/config/usb_gadget/g/bDeviceClass
echo 0x00 > /sys/kernel/config/usb_gadget/g/bDeviceSubClass
echo 0x00 > /sys/kernel/config/usb_gadget/g/bDeviceProtocol
echo 0x0040 > /sys/kernel/config/usb_gadget/g/bMaxPacketSize0
echo '0' > /sys/kernel/config/usb_gadget/g/strings/0x409/serialnumber
echo 'NUVOTON' > /sys/kernel/config/usb_gadget/g/strings/0x409/manufacturer
echo 'WPM USB' > /sys/kernel/config/usb_gadget/g/strings/0x409/product
echo 0x32 > /sys/kernel/config/usb_gadget/g/configs/c.1/MaxPower
echo 0xC0 > /sys/kernel/config/usb_gadget/g/configs/c.1/bmAttributes
echo 'Default Configuration' > /sys/kernel/config/usb_gadget/g/configs/c.1/strings/0x409/configuration
echo 0x00 > /sys/kernel/config/usb_gadget/g/functions/hid.usb0/protocol
echo 54 > /sys/kernel/config/usb_gadget/g/functions/hid.usb0/report_length
echo 0x00 > /sys/kernel/config/usb_gadget/g/functions/hid.usb0/subclass
echo '05010900a101150025ff190029ff954075088102190029ff9102c0' | xxd -r -ps > /sys/kernel/config/usb_gadget/g/functions/hid.usb0/report_desc
ln -s /sys/kernel/config/usb_gadget/g/functions/hid.usb0 /sys/kernel/config/usb_gadget/g/configs/c.1
udevadm settle -t 5 || :
ls /sys/class/udc/ > /sys/kernel/config/usb_gadget/g/UDC
