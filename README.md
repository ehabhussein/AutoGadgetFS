<pre>
# AutoGadgetFS
Usb testing framework

Work In progress. will be documented when the project is launched. 


# python3 autogfs.py   

       *******************************************************************************. 
       *AutoGadgetFS: Automated USB testing based on gadgetfs*************************. 
       *******************************************************************************.      
        
Welcome to the AutoGFS shell.   Type help or ? to list commands.  

Agfs> help. 

Documented commands (type help <topic>):  
========================================
devProxy  find_usb_devices  help            searchMsg       
exit      get_device_info   release_device  usblyzerparse    

Agfs> help find_usb_devices  
Find and select your usb device  
Agfs> help searchMsg  
This function allows you to search and select messages from the db for usage
Agfs> help usblyzerparse
Parses the XML export from USBlyzer and puts it into an sqlite database
Pass a db name to it
Agfs> help find_usb_devices
Find and select your usb device
Agfs> help release_device
releases the claimed device back to its kernel driver
Agfs> find_usb_devices()
0 : VIA Labs, Inc.:2071:8457
1 : Linux 5.2.0-kali2-amd64 xhci-hcd:3:7531
2 : Linux 5.2.0-kali2-amd64 xhci-hcd:2:7531
3 : Linux 5.2.0-kali2-amd64 xhci-hcd:3:7531
4 : NUVOTON:41750:1046
5 : VIA Technologies Inc.         :258:8457
6 : Logitech:50484:1133
7 : VIA Labs, Inc.:10263:8457
8 : None:57506:1161
9 : CN09357GLOG008CLA8P2A01:26403:3141
10 : Linux 5.2.0-kali2-amd64 xhci-hcd:2:7531
---> Select a device: 4
DEVICE ID 0416:a316 on Bus 001 Address 033 =================
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
Do you want pyUSB to claim the device interface: [y/n] y
Checking HID report retreval

05010900a101150025ff190029ff954075088102190029ff9102c0
Success, now you can use the setupGadgetFS() method to use the device with GadgetFS
Agfs> usblyzerparse('mydbname')
Creating Tables
Enter Path to USBlyzer xml dump: 1.xml
Parsing the file..
Inserting into database..
Agfs> searchMsg()
id->Column
{0: 'seq',
 1: 'io',
 2: 'cie',
 3: 'DevObjAddr',
 4: 'irpaddr',
 5: 'RawDataSize',
 6: 'RawData',
 7: 'RawAscii',
 8: 'replyfrom'}
Search in which column id: 0
Enter search text: 2233
{0: (2233, 'in', '01:01:81', 'FFFFDC84413762C0h', 'FFFFDC844619F9A0h', 0, '', '', 0),
 1: (12233, 'in', '01:01:81', 'FFFFDC844176BAD0h', 'FFFFDC844619F9A0h', 0, '', '', 0),
 2: (22233, 'in', '01:01:81', 'FFFFDC8441F02E10h', 'FFFFDC844619F9A0h', 64, '96140000EC0400007FFFFFFF00F00100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', '\x96\x14\x00\x00ì\x04\x00\x00\x7fÿÿÿ\x00ð\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 22218),
 3: (22330, 'out', '01:01:02', 'FFFFDC84413762C0h', 'FFFFDC844C9149A0h', 64, '00000000F704000005233C3203210D20F8F791F918E0444A0523443203210D20F8F789F910E0404A05234C3203210720F8F781F908E03C4A0523543203210D20', '\x00\x00\x00\x00÷\x04\x00\x00\x05#<2\x03!\r ø÷\x91ù\x18àDJ\x05#D2\x03!\r ø÷\x89ù\x10à@J\x05#L2\x03!\x07 ø÷\x81ù\x08à<J\x05#T2\x03!\r ', 0),
 4: (22331, 'out', '01:01:02', 'FFFFDC84413762C0h', 'FFFFDC844C9149A0h', 0, '', '', 22330),
 5: (22332, 'out', '01:01:02', 'FFFFDC8441F02E10h', 'FFFFDC844C9149A0h', 0, '', '', 22329),
 6: (22333, 'out', '01:01:02', 'FFFFDC844176BAD0h', 'FFFFDC844C9149A0h', 0, '', '', 22328),
 7: (22334, 'in', '01:01:81', 'FFFFDC84413762C0h', 'FFFFDC8442BED9A0h', 64, '6F170000F60400007FFFFFFF00F00100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'o\x17\x00\x00ö\x04\x00\x00\x7fÿÿÿ\x00ð\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 22321),
 8: (22335, 'in', '01:01:81', 'FFFFDC8441F02E10h', 'FFFFDC8442BED9A0h', 64, '6F170000F60400007FFFFFFF00F00100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'o\x17\x00\x00ö\x04\x00\x00\x7fÿÿÿ\x00ð\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 22320),
 9: (22336, 'in', '01:01:81', 'FFFFDC844176BAD0h', 'FFFFDC8442BED9A0h', 64, '6F170000F60400007FFFFFFF00F00100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'o\x17\x00\x00ö\x04\x00\x00\x7fÿÿÿ\x00ð\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 22319),
 10: (22337, 'in', '01:01:81', 'FFFFDC844176BAD0h', 'FFFFDC8442BED9A0h', 0, '', '', 0),
 11: (22338, 'in', '01:01:81', 'FFFFDC8441F02E10h', 'FFFFDC8442BED9A0h', 0, '', '', 0),
 12: (22339, 'in', '01:01:81', 'FFFFDC84413762C0h', 'FFFFDC8442BED9A0h', 0, '', '', 0),
 13: (32233, 'out', '01:01:02', 'FFFFDC844176BAD0h', 'FFFFDC844C9149A0h', 0, '', '', 32228),
 14: (42233, 'in', '01:01:81', 'FFFFDC844176BAD0h', 'FFFFDC8442BED9A0h', 0, '', '', 0)}
Which message id to select: 1
(12233, 'in', '01:01:81', 'FFFFDC844176BAD0h', 'FFFFDC844619F9A0h', 0, '', '', 0)
Agfs> 
</pre>
