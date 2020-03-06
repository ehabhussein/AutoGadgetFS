![intro.png](attachment:intro.png)


```python
import libagfs
```


```python
x =  libagfs.agfs()
```

    [37m***************************************
    * AutoGadgetFS: USB testing made easy *
    ***************************************[0m



```python
x.findSelect()
```

    Give your project a name?!: Demo1
    0 : Linux 5.4.0-kali4-amd64 xhci-hcd:3:7531
    1 : Linux 5.4.0-kali4-amd64 xhci-hcd:2:7531
    2 : VIA Labs, Inc.:2071:8457
    3 : Linux 5.4.0-kali4-amd64 xhci-hcd:3:7531
    4 : Nuvoton:20764:1046
    5 : None:57506:1161
    6 : CN09357GLOG008CLA8P2A01:26403:3141
    7 : SINO WEALTH:4102:9610
    8 : VIA Technologies Inc.         :258:8457
    9 : Logitech:50475:1133
    10 : VIA Labs, Inc.:10263:8457
    11 : Linux 5.4.0-kali4-amd64 xhci-hcd:2:7531
    ---> Select a device: 4
    DEVICE ID 0416:511c on Bus 001 Address 012 =================
     bLength                :   0x12 (18 bytes)
     bDescriptorType        :    0x1 Device
     bcdUSB                 :  0x110 USB 1.1
     bDeviceClass           :    0x0 Specified at interface
     bDeviceSubClass        :    0x0
     bDeviceProtocol        :    0x0
     bMaxPacketSize0        :   0x40 (64 bytes)
     idVendor               : 0x0416
     idProduct              : 0x511c
     bcdDevice              :  0x100 Device 1.0
     iManufacturer          :    0x1 Nuvoton
     iProduct               :    0x2 Nu-Link
     iSerialNumber          :    0x0 
     bNumConfigurations     :    0x1
      CONFIGURATION 1: 100 mA ==================================
       bLength              :    0x9 (9 bytes)
       bDescriptorType      :    0x2 Configuration
       wTotalLength         :   0x40 (64 bytes)
       bNumInterfaces       :    0x2
       bConfigurationValue  :    0x1
       iConfiguration       :    0x0 
       bmAttributes         :   0x80 Bus Powered
       bMaxPower            :   0x32 (100 mA)
        INTERFACE 0: Human Interface Device ====================
         bLength            :    0x9 (9 bytes)
         bDescriptorType    :    0x4 Interface
         bInterfaceNumber   :    0x0
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
           bInterval        :    0x1
          ENDPOINT 0x2: Interrupt OUT ==========================
           bLength          :    0x7 (7 bytes)
           bDescriptorType  :    0x5 Endpoint
           bEndpointAddress :    0x2 OUT
           bmAttributes     :    0x3 Interrupt
           wMaxPacketSize   :   0x40 (64 bytes)
           bInterval        :    0x1
        INTERFACE 1: CDC Data ==================================
         bLength            :    0x9 (9 bytes)
         bDescriptorType    :    0x4 Interface
         bInterfaceNumber   :    0x1
         bAlternateSetting  :    0x0
         bNumEndpoints      :    0x2
         bInterfaceClass    :    0xa CDC Data
         bInterfaceSubClass :    0x0
         bInterfaceProtocol :    0x0
         iInterface         :    0x0 
          ENDPOINT 0x83: Bulk IN ===============================
           bLength          :    0x7 (7 bytes)
           bDescriptorType  :    0x5 Endpoint
           bEndpointAddress :   0x83 IN
           bmAttributes     :    0x2 Bulk
           wMaxPacketSize   :   0x40 (64 bytes)
           bInterval        :    0x0
          ENDPOINT 0x4: Bulk OUT ===============================
           bLength          :    0x7 (7 bytes)
           bDescriptorType  :    0x5 Endpoint
           bEndpointAddress :    0x4 OUT
           bmAttributes     :    0x2 Bulk
           wMaxPacketSize   :   0x40 (64 bytes)
           bInterval        :    0x0
    do you want to detach the device from it's kernel driver: [y/n] y
    Disabling Interfaces on configuration: 1
    Disabling interfaces :
    	2
    Disabled interface: 0
    [-] Kernel driver detached
    Configuration Value: 1
    
    	Interface number: 0,Alternate Setting: 0
    
    		Endpoint Address: 0x81
    
    		Endpoint Address: 0x2
    
    	Interface number: 1,Alternate Setting: 0
    
    		Endpoint Address: 0x83
    
    		Endpoint Address: 0x4
    
    Do you want to reset the device? [y/n]: n
    which Configuration would you like to use: 1
    which Interface would you like to use: 0
    which Alternate setting would you like to use: 0
    which Endpoint IN would you like to use: 0x81
    which Endpoint OUT would you like to use: 0x2
    Checking if device supports DFU mode based on USB DFU R1.1
    [32m***************************************
    * This Device doesnt support DFU mode *
    ***************************************[0m
    Do you want to claim the device interface: [y/n] y
    Checking HID report retrieval
    
    b'05010900a101150026ff0019002900750895408102190029009102c0'
    .........ÿ.....u...........À
    Do you want to save this device's information?[y/n]y
    setting up: Nuvoton
    Creating backup of device
    
    - Done: Device settings copied to file.
    



```python
print(hex(x.epin))
print(hex(x.epout))
print(x.SelectedDevice)
```

    0x81
    0x2
    Demo1-Nuvoton-1046-20764-1583520221.3661065



```python
#Configure and setup the usb gadget
#below image is of the host machine that the pi zero is connected to prior to running the gadget
```

![setgfs1.png](attachment:setgfs1.png)


```python
x.setupGadgetFS()
```

    setting up: Nuvoton
    Aquiring info about the device for Gadetfs
    
    are you going to configure this gadget to work with windows [y/n] ?y
    0 ]  b'05010900a101150026ff0019002900750895408102190029009102c0'
    1 ]  b''
    Which report would you like to use? 0
    - Creating Bash script!
    
    - Done wrote bash script. Try testing your gadget
    
    Do you want to push the gadget to the Pi zero ?[y/n] y
    Enter the ip address of the Pi zero: 192.168.254.126
    Enter the port of the Pi zero: 22
    Enter the username: pi
    ········
    Connecting...
    Sending...
    Done!
    Do you want to run the gadget? [y/n]y
    [34m********************************
    * Gadget should now be running *
    ********************************[0m


![setgfs2.png](attachment:setgfs2.png)


```python
#Start the router on the pi zero:
    # ssh into the pi zero and run the router.py
        # the option -l defines the Max packet size
        # the option -ip is the ip address of the rabbitMQ server
```

![pizero-run-router.png](attachment:pizero-run-router.png)

start the software that uses the device on the host machine
![nuvo.png](attachment:nuvo.png)


```python
#start the man in the middle sniffing
x.startMITMusbWifi()
```

    Connected to RabbitMQ, starting consumption!
    Connected to exchange, we can send to host!
    VVV++++++++++++++++FROM HOST
     b'\x01>\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    VVV++++++++++++++++FROM HOST
     b'\x02>\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    VVV++++++++++++++++FROM HOST
     b'\x03\x14\xfb\x00\x00\x00\x01\xff\x00\x00\x00\x01\x00P\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x1d\x98\xf0\x86\x02\x07\x98R\xd0\x91\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\x04\x14\xfb\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00P\x04\x00\x00\x00\xfb\xff\xff\xff\x00\x00\x1d\x98\xf0\x86\x02\x07\x98R\xd0\x91\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\x05\x14\xfb\x00\x00\x00\x01\x00\xff\xff\x00\xc0\x00P1\x00\x00\x00\xce\xff\xff\xff\x00\x00\x1d\x98\xf0\x86\x02\x07\x98R\xd0\x91\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\x06\x14\xfb\x00\x00\x00\x01\xff\x00\x00\x10\xc0\x00P\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x1d\x98\xf0\x86\x02\x07\x98R\xd0\x91\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\x07,\xfb\x00\x00\x00\x03\x00\x00\x17\x0c\xc0\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x04\xc0\x00P\x10\x00\x10\x00\x00\x00\x00\x00\x10\xc0\x00P\x01\x00\x00\x00\x00\x00\x00\x00m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\x08\x14\xfb\x00\x00\x00\x01\xff\x00\x00\x10\xc0\x00P\x00\x00\x00\x00\xff\xff\xff\xff6+\xcb]\x00\x00\x02\x07\x98R\xd0\x91\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\t \xfb\x00\x00\x00\x02\xff\x00\x00\x00\xc0\x00P\x00\x00\x00\x00\xff\xff\xff\xff\x08\xc0\x00P\x00\x00\x00\x00\xff\xff\xff\xff\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\n\x14\xfb\x00\x00\x00\x01\xff\x00\xff\x00\x01\x00P\x00\x00\x00\x00\xff\xff\xff\xff6+\xcb]\x00\x00\x02\x07\x98R\xd0\x91\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\x0b\x14\xfb\x00\x00\x00\x01\x00\x00\xff\x00\xc0\x00P\xfe\xff\xff\xff\xfe\xff\xff\xff6+\xcb]\x00\x00\x02\x07\x98R\xd0\x91\x8f\x12=\xd1\xd4\x81\xa8\x9b\xe7\xb8\xf2\x06m\xcc\xcab-\xed{\x18F\xd5\xab\xec\xe3\xe1\x0e\xb0\xab,'
    VVV++++++++++++++++FROM HOST
     b'\x01>\xff\xff\xff\xff\xdb\x1a\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    VVV++++++++++++++++FROM HOST
     b'\x02>\xff\xff\xff\xff\xdb\x1a\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'


![mitmfrom%20device.png](attachment:mitmfrom%20device.png)


```python
#Host side software has successfully connected to the device and you can sniff traffic bidirectional
```

![mitmconnected.png](attachment:mitmconnected.png)


```python
#stop man in the middle
x.stopMITMusbWifi()
```

    [32m**********************************
    * Thread Terminated Successfully *
    **********************************[0m
    [32m**************************************
    * Sniffing has stopped successfully! *
    **************************************[0m
    [32m***********************
    * MITM Proxy stopped! *
    ***********************[0m
    [32m***************************************
    * MITM Proxy has now been terminated! *
    ***************************************[0m



```python
#clear all the rabbitMQ queues
x.clearqueues()
```

    cleared todevice queue
    cleared tohost queue
    cleared tonull queue
    cleared edap queues



```python
#enumerate possible control transfer requests on the device
    #the fuzz param:
        #fast -> limited bmRequests
        #full -> the full monty , takes time and is somewhat dangerous due to set requests
        #results are stored in the folder devEnumCT/
x.devEnumCtrltrnsf(fuzz='fast')
```

    [32m***********
    * started *
    ***********[0m
    [5m[34m*************************
    * Now at bmRequest 0x81 *
    *************************[0m
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x00 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x01 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x02 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x03 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x04 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x05 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x06 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x07 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x08 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x09 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x0A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x0B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x0C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x0D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x0E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x0F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x10 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x11 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x12 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x13 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x14 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x15 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x16 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x17 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x18 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x19 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x1A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x1B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x1C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x1D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x1E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x1F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x20 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x21 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x22 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x23 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x24 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x25 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x26 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x27 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x28 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x29 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x2A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x2B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x2C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x2D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x2E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x2F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x30 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x31 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x32 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x33 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x34 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x35 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x36 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x37 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x38 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x39 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x3A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x3B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x3C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x3D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x3E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x3F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x40 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x41 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x42 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x43 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x44 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x45 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x46 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x47 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x48 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x49 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x4A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x4B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x4C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x4D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x4E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x4F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x50 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x51 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x52 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x53 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x54 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x55 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x56 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x57 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x58 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x59 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x5A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x5B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x5C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x5D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x5E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x5F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x60 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x61 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x62 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x63 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x64 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x65 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x66 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x67 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x68 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x69 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x6A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x6B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x6C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x6D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x6E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x6F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x70 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x71 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x72 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x73 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x74 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x75 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]


    /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:6: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
      


    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x76 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x77 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x78 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x79 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x7A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x7B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x7C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x7D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x7E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x7F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x80 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x81 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x82 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x83 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x84 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x85 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x86 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x87 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x88 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x89 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x8A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x8B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x8C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x8D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x8E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x8F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x90 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x91 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x92 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x93 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x94 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x95 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x96 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x97 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x98 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x99 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x9A , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x9B , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x9C , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x9D , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x9E , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0x9F , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA0 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA1 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA2 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA3 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA4 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA5 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA6 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA7 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA8 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xA9 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xAA , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xAB , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xAC , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xAD , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xAE , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xAF , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB0 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB1 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB2 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB3 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB4 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB5 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB6 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB7 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB8 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xB9 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xBA , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xBB , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xBC , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xBD , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xBE , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xBF , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC0 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC1 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC2 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC3 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC4 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC5 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC6 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC7 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC8 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xC9 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xCA , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xCB , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xCC , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xCD , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xCE , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xCF , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD0 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD1 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD2 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD3 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD4 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD5 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD6 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD7 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD8 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xD9 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xDA , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xDB , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xDC , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xDD , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xDE , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xDF , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE0 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE1 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE2 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE3 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE4 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE5 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE6 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE7 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE8 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xE9 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xEA , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xEB , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xEC , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xED , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xEE , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xEF , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF0 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF1 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF2 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF3 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF4 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF5 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF6 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF7 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF8 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xF9 , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xFA , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xFB , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xFC , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xFD , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xFE , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x00,wValue=0xFF , wIndex=0x00, data_length=0xfff
    received: b'\x00\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x00 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x01 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x02 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x03 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x04 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x05 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x06 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x07 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x08 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x09 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x0A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x0B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x0C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x0D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x0E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x0F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x10 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x11 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x12 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x13 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x14 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x15 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x16 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x17 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x18 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x19 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x1A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x1B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x1C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x1D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x1E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x1F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x20 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x21 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x22 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x23 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x24 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x25 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x26 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x27 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x28 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x29 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x2A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x2B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x2C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x2D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x2E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x2F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x30 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x31 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x32 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x33 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x34 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x35 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x36 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x37 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x38 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x39 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x3A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x3B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x3C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x3D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x3E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x3F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x40 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x41 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x42 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x43 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x44 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x45 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x46 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x47 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x48 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x49 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x4A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x4B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x4C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x4D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x4E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x4F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x50 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x51 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x52 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x53 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x54 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x55 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x56 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x57 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x58 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x59 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x5A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x5B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x5C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x5D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x5E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x5F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x60 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x61 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x62 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x63 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x64 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x65 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x66 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x67 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x68 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x69 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x6A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x6B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x6C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x6D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x6E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x6F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x70 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x71 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x72 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x73 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x74 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x75 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x76 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x77 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x78 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x79 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x7A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x7B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x7C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x7D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x7E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x7F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x80 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x81 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x82 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x83 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x84 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x85 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x86 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x87 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x88 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x89 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x8A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x8B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x8C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x8D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x8E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x8F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x90 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x91 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x92 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x93 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x94 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x95 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x96 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x97 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x98 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x99 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x9A , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x9B , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x9C , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x9D , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x9E , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0x9F , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA0 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA1 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA2 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA3 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA4 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA5 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA6 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA7 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA8 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xA9 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xAA , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xAB , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xAC , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xAD , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xAE , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xAF , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB0 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB1 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB2 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB3 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB4 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB5 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB6 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB7 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB8 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xB9 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xBA , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xBB , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xBC , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xBD , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xBE , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xBF , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC0 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC1 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC2 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC3 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC4 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC5 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC6 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC7 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC8 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xC9 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xCA , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xCB , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xCC , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xCD , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xCE , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xCF , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD0 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD1 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD2 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD3 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD4 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD5 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD6 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD7 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD8 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xD9 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xDA , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xDB , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xDC , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xDD , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xDE , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xDF , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE0 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE1 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE2 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE3 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE4 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE5 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE6 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE7 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE8 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xE9 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xEA , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xEB , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xEC , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xED , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xEE , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xEF , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF0 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF1 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF2 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF3 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF4 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF5 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF6 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF7 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF8 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xF9 , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xFA , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xFB , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xFC , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xFD , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xFE , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x08,wValue=0xFF , wIndex=0x00, data_length=0xfff
    received: b'\x01'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x00 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x01 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x02 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x03 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x04 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x05 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x06 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x07 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x08 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x09 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x0A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x0B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x0C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x0D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x0E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x0F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x10 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x11 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x12 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x13 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x14 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x15 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x16 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x17 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x18 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x19 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x1A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x1B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x1C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x1D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x1E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x1F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x20 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x21 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x22 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x23 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x24 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x25 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x26 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x27 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x28 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x29 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x2A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x2B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x2C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x2D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x2E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x2F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x30 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x31 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x32 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x33 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x34 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x35 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x36 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x37 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x38 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x39 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x3A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x3B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x3C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x3D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x3E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x3F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x40 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x41 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x42 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x43 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x44 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x45 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x46 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x47 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x48 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x49 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x4A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x4B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x4C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x4D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x4E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x4F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x50 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x51 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x52 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x53 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x54 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x55 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x56 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x57 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x58 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x59 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x5A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x5B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x5C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x5D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x5E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x5F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x60 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x61 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x62 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x63 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x64 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x65 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x66 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x67 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x68 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x69 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x6A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x6B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x6C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x6D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x6E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x6F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x70 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x71 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x72 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x73 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x74 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x75 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x76 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x77 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x78 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x79 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x7A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x7B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x7C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x7D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x7E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x7F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x80 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x81 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x82 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x83 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x84 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x85 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x86 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x87 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x88 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x89 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x8A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x8B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x8C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x8D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x8E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x8F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x90 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x91 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x92 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x93 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x94 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x95 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x96 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x97 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x98 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x99 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x9A , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x9B , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x9C , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x9D , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x9E , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0x9F , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA0 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA1 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA2 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA3 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA4 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA5 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA6 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA7 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA8 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xA9 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xAA , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xAB , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xAC , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xAD , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xAE , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xAF , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB0 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB1 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB2 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB3 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB4 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB5 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB6 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB7 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB8 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xB9 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xBA , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xBB , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xBC , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xBD , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xBE , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xBF , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC0 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC1 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC2 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC3 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC4 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC5 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC6 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC7 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC8 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xC9 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xCA , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xCB , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xCC , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xCD , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xCE , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xCF , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD0 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD1 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD2 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD3 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD4 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD5 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD6 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD7 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD8 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xD9 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xDA , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xDB , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xDC , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xDD , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xDE , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xDF , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE0 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE1 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE2 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE3 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE4 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE5 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE6 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE7 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE8 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xE9 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xEA , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xEB , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xEC , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xED , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xEE , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xEF , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF0 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF1 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF2 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF3 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF4 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF5 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF6 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF7 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF8 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xF9 , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xFA , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xFB , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xFC , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xFD , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xFE , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    *******************************
    Found Valid Control Transfer request on device: Demo1-Nuvoton-1046-20764-1583520221.3661065
    bmRequest=0x81, bRequest=0x0A,wValue=0xFF , wIndex=0x00, data_length=0xfff
    received: b'\x00'...[SNIP]
    [5m[34m*************************
    * Now at bmRequest 0xc0 *
    *************************[0m
    [32m**********
    * Ended! *
    **********[0m



```python
#send a control transfer request to the device
    #devctrltrnsf(bmRequestType, bRequest, wValue, wIndex, wLength)
    #or
    #x.device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
response = x.device.ctrl_transfer(0x81,0x6,0x2200,0,0xA)
import binascii
print(binascii.hexlify(response))
```

    b'05010900a101150026ff'



```python
#Send random packets to the device
#def devrandfuzz(self, howmany=1000, size='fixed',timeout=0.5):
#        """
#        this method allows you to create fixed or random size packets created using urandom
#        :param howmany: how many packets to be sent to the device`
#        :param size: string value whether its fixed or random size
#        :param timeout: timeOUT !
#        :return: None
#        """
x.devrandfuzz(howmany=3,size='fixed')
```

    ****************VVV Packet #0  VVV**********************
    sent-->
     b'e75bb5bfe4dbe5e2cfa142def9cc2c6bd2f743aacd0028a564da17fefd91262ba7422258e1dad69a87f54b415e1ecfca9a554840b5f89f91b9713b8dcb4b5215'
    received -->
     b'e7040000000009200100000288778e01860100b20000362bcb5d000002079852d0918f123dd1d481a89be7b8f2066dccca622ded7b1846d5abece3e10eb0ab2c'


    /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:10: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
      # Remove the CWD from sys.path while we load stuff.


    ****************VVV Packet #1  VVV**********************
    sent-->
     b'469599b163bf006135faa4237516ad27f515a34d1f2f25ae752fd89405af46bc20fdf033d45d8e4b6b19faf0f660d438a170c0d5557dd40977a7086b3ad827c4'
    received -->
     b'c6040000000009200100000288778e01860100b20000362bcb5d000002079852d0918f123dd1d481a89be7b8f2066dccca622ded7b1846d5abece3e10eb0ab2c'
    ****************VVV Packet #2  VVV**********************
    sent-->
     b'88a3d8dd3d70ddd2981883d15708da53fc754b8c477a15b5bfaa491558c8cdeda7ba6d13550cbe168e8a562f329dfe1fc6eefba8801b0d9a8dafec9a127db00c'
    received -->
     b'88040000000009200100000288778e01860100b20000362bcb5d000002079852d0918f123dd1d481a89be7b8f2066dccca622ded7b1846d5abece3e10eb0ab2c'



```python
x.devrandfuzz(howmany=3,size='random')
```

    ****************VVV Packet #0  VVV**********************
    sent-->
     b'474e90cfc50352995166fd75a752825c611116349801f91203'
    received -->
     b'c7040000000009200100000288778e01860100b20000362bcb5d000002079852d0918f123dd1d481a89be7b8f2066dccca622ded7b1846d5abece3e10eb0ab2c'


    /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:1: DeprecationWarning: tostring() is deprecated. Use tobytes() instead.
      """Entry point for launching an IPython kernel.


    ****************VVV Packet #1  VVV**********************
    sent-->
     b'8b2388756d8dcd8bf48388d25f53c6e8c60d30e8d4e1437e7ff7c715'
    received -->
     b'8b040000000009200100000288778e01860100b20000362bcb5d000002079852d0918f123dd1d481a89be7b8f2066dccca622ded7b1846d5abece3e10eb0ab2c'
    ****************VVV Packet #2  VVV**********************
    sent-->
     b'804ed054324502d65f14746bdb419121047c9de62ed14d596b6f4e36db68b5b81f765c3cef'
    received -->
     b'80040000000009200100000288778e01860100b20000362bcb5d000002079852d0918f123dd1d481a89be7b8f2066dccca622ded7b1846d5abece3e10eb0ab2c'



```python
#Send random packets to the host
#    def hstrandfuzz(self, howmany=1, size=None, min=None, max = None, timeout=0.5):
#        """
#        this method allows you to create fixed or random size packets created using urandom
#        :param howmany: how many packets to be sent to the device`
#        :param size: fixed size packet
#        size = 10 to generate a length 10 packet 
#        :param min minimum size value to generate a packet
#        :param max maximum size value to generate a packet
#        :param timeout: timeOUT !
#        :return: None
#        """

x.hostwrite("aaaaaA")

x.hostwrite("aaaaaA")
x.hostwrite("0A0B0C0D")
```

    [34m*****************************
    * Queues to host are yours! *
    *****************************[0m


**packets have been received from the queue and sent over to the host machine
![hostwrite.png](attachment:hostwrite.png)


```python
x.stopQueuewrite()
```


```python
#create a new project
x.newProject()
```

    [-] Releasing the Interface
    Releasing interfaces :
    	2
    [-] Attaching the kernel driver
    Releasing interface: 0
    Releasing interface: 1
    Releasing interface: 2
    [-] Device released!
    Give your project a name?!: sdfsdf
    0 : Linux 5.4.0-kali4-amd64 xhci-hcd:3:7531
    1 : Linux 5.4.0-kali4-amd64 xhci-hcd:2:7531
    2 : VIA Labs, Inc.:2071:8457
    3 : Linux 5.4.0-kali4-amd64 xhci-hcd:3:7531
    4 : Logitech:50484:1133
    5 : None:57506:1161
    6 : CN09357GLOG008CLA8P2A01:26403:3141
    7 : SINO WEALTH:4102:9610
    8 : VIA Technologies Inc.         :258:8457
    9 : Logitech:50475:1133
    10 : VIA Labs, Inc.:10263:8457
    11 : Linux 5.4.0-kali4-amd64 xhci-hcd:2:7531
    ---> Select a device: 4
    DEVICE ID 046d:c534 on Bus 001 Address 013 =================
     bLength                :   0x12 (18 bytes)
     bDescriptorType        :    0x1 Device
     bcdUSB                 :  0x200 USB 2.0
     bDeviceClass           :    0x0 Specified at interface
     bDeviceSubClass        :    0x0
     bDeviceProtocol        :    0x0
     bMaxPacketSize0        :    0x8 (8 bytes)
     idVendor               : 0x046d
     idProduct              : 0xc534
     bcdDevice              : 0x2900 Device 41.0
     iManufacturer          :    0x1 Logitech
     iProduct               :    0x2 USB Receiver
     iSerialNumber          :    0x0 
     bNumConfigurations     :    0x1
      CONFIGURATION 1: 98 mA ===================================
       bLength              :    0x9 (9 bytes)
       bDescriptorType      :    0x2 Configuration
       wTotalLength         :   0x3b (59 bytes)
       bNumInterfaces       :    0x2
       bConfigurationValue  :    0x1
       iConfiguration       :    0x4 RQR29.00_B0015
       bmAttributes         :   0xa0 Bus Powered, Remote Wakeup
       bMaxPower            :   0x31 (98 mA)
        INTERFACE 0: Human Interface Device ====================
         bLength            :    0x9 (9 bytes)
         bDescriptorType    :    0x4 Interface
         bInterfaceNumber   :    0x0
         bAlternateSetting  :    0x0
         bNumEndpoints      :    0x1
         bInterfaceClass    :    0x3 Human Interface Device
         bInterfaceSubClass :    0x1
         bInterfaceProtocol :    0x1
         iInterface         :    0x0 
          ENDPOINT 0x81: Interrupt IN ==========================
           bLength          :    0x7 (7 bytes)
           bDescriptorType  :    0x5 Endpoint
           bEndpointAddress :   0x81 IN
           bmAttributes     :    0x3 Interrupt
           wMaxPacketSize   :    0x8 (8 bytes)
           bInterval        :    0x8
        INTERFACE 1: Human Interface Device ====================
         bLength            :    0x9 (9 bytes)
         bDescriptorType    :    0x4 Interface
         bInterfaceNumber   :    0x1
         bAlternateSetting  :    0x0
         bNumEndpoints      :    0x1
         bInterfaceClass    :    0x3 Human Interface Device
         bInterfaceSubClass :    0x1
         bInterfaceProtocol :    0x2
         iInterface         :    0x0 
          ENDPOINT 0x82: Interrupt IN ==========================
           bLength          :    0x7 (7 bytes)
           bDescriptorType  :    0x5 Endpoint
           bEndpointAddress :   0x82 IN
           bmAttributes     :    0x3 Interrupt
           wMaxPacketSize   :   0x14 (20 bytes)
           bInterval        :    0x2
    do you want to detach the device from it's kernel driver: [y/n] y
    Disabling Interfaces on configuration: 1
    Disabling interfaces :
    	2
    Disabled interface: 0
    Disabled interface: 1
    [-] Kernel driver detached
    Configuration Value: 1
    
    	Interface number: 0,Alternate Setting: 0
    
    		Endpoint Address: 0x81
    
    	Interface number: 1,Alternate Setting: 0
    
    		Endpoint Address: 0x82
    
    Do you want to reset the device? [y/n]: n
    which Configuration would you like to use: 1
    which Interface would you like to use: 0
    which Alternate setting would you like to use: 0
    which Endpoint IN would you like to use: 0x81
    which Endpoint OUT would you like to use: 0x82
    Checking if device supports DFU mode based on USB DFU R1.1
    [32m***************************************
    * This Device doesnt support DFU mode *
    ***************************************[0m
    Do you want to claim the device interface: [y/n] y
    Checking HID report retrieval
    
    b'05010906a101050719e029e71500250175019508810281039505050819012905910295017503910195067508150026a400050719002aa4008100c0'
    .........à.ç....u...................u.....u...............À
    Do you want to save this device's information?[y/n]n



```python
x.setupGadgetFS()
```

    setting up: Logitech
    Aquiring info about the device for Gadetfs
    
    are you going to configure this gadget to work with windows [y/n] ?y
    0 ]  b'05010906a101050719e029e71500250175019508810281039505050819012905910295017503910195067508150026a400050719002aa4008100c0'
    1 ]  b'05010902a10185020901a1000509190129101500250195107501810205011601f826ff07750c95020930093181061581257f7508950109388106050c0a380295018106c0c0050c0901a1018503751095021501268c0219012a8c028100c005010980a10185047502950115012503098209810983816075068103c00600ff0901a101851075089506150026ff000901810009019100c00600ff0902a101851175089513150026ff000902810009029100c0'
    Which report would you like to use? 0
    - Creating Bash script!
    
    - Done wrote bash script. Try testing your gadget
    
    Do you want to push the gadget to the Pi zero ?[y/n] y
    Enter the ip address of the Pi zero: pi
    Enter the port of the Pi zero: 22
    Enter the username: pi
    ········
    Connecting...
    Sending...
    Done!
    Do you want to run the gadget? [y/n]y
    [34m********************************
    * Gadget should now be running *
    ********************************[0m



```python
#Sniff the endpoint IN interface send it to the queue or to a pesudo terminal
#def startSniffReadThread(self,endpoint=None, pts=None, queue=None,timeout=0,genpkts=0,savetofile=0):
#       """ This is a thread to continuously read the replies from the device and dependent on what you pass to the method either pts or queue
#       :param endpoint: endpoint address you want to read from
#       :param pts: if you want to read the device without queues and send output to a specific tty
#       :param queue: if you will use the queues for a full proxy between target and host
#       :param channel: this is automatically passed if you use the self.startMITMusbWifi()
#       :param savetofile: fill in ********************
#       :param genpkts: fill in ********************
#       :return: None
#       """

x.startSniffReadThread(endpoint=x.epin,pts=1)
```

    Open a new terminal and type 'tty' and input the pts number: (/dev/pts/X) /dev/pts/3
    Press Enter when ready..on /dev/pts/3


![keyboard-mouse.png](attachment:keyboard-mouse.png)


```python
#stop the sniffing
x.stopSniffing()
```

    [32m**************************************
    * Sniffing has stopped successfully! *
    **************************************[0m


![keyboard-mouse2.png](attachment:keyboard-mouse2.png)


```python
#send random generated packets to the host
 #def hstrandfuzz(self, howmany=1, size=None, min=None, max = None, timeout=0.5):
 #       """
 #       this method allows you to create fixed or random size packets created using urandom
 #       :param howmany: how many packets to be sent to the device`
 #       :param size: fixed size packet length
 #                    size = 10 to generate a length 10 packet
 #       :param min minimum size value to generate a packet
 #       :param max maximum size value to generate a packet
 #       :param timeout: timeOUT !
 #       :return: None
 #       """
x.hstrandfuzz(howmany=3,size=8,timeout=0)
```

    [34m*****************************
    * Queues to host are yours! *
    *****************************[0m
    [34m*****************************
    * Queues to host are yours! *
    *****************************[0m
    ****************VVV Packet #0  VVV**********************
    sent-->
     b'bc1a1aa32092ef0d'
    ****************VVV Packet #1  VVV**********************
    sent-->
     b'591f4089ecdb9f9f'
    ****************VVV Packet #2  VVV**********************
    sent-->
     b'4f2fa6601689be80'


    Exception in thread Thread-156:
    Traceback (most recent call last):
      File "/usr/lib/python3.7/threading.py", line 926, in _bootstrap_inner
        self.run()
      File "/usr/lib/python3.7/threading.py", line 870, in run
        self._target(*self._args, **self._kwargs)
      File "/home/raindrop/PycharmProjects/AutoGadgetFs/libagfs.py", line 468, in rabbitmqfakeheartbeat
        if self.hbkill == 1:
      File "/usr/local/lib/python3.7/dist-packages/pika/adapters/blocking_connection.py", line 2247, in basic_publish
        mandatory=mandatory)
      File "/usr/local/lib/python3.7/dist-packages/pika/channel.py", line 421, in basic_publish
        self._raise_if_not_open()
      File "/usr/local/lib/python3.7/dist-packages/pika/channel.py", line 1389, in _raise_if_not_open
        raise exceptions.ChannelWrongStateError('Channel is closed.')
    pika.exceptions.ChannelWrongStateError: Channel is closed.
    


**Packet received from Queue and sent to the host machine
![keyboard-mouse4.png](attachment:keyboard-mouse4.png)

**Packet showed in host machine
![keyboard-mouse3.png](attachment:keyboard-mouse3.png)


```python
#Release the device and attach the kernel drivers
x.releasedev()
```

    [-] Releasing the Interface
    Releasing interfaces :
    	2
    [-] Attaching the kernel driver
    Releasing interface: 0
    Interface reattached
    Releasing interface: 1
    Interface reattached
    Releasing interface: 2
    [-] Device released!



```python
#New project with a device that leaks data when requesting the HID report with the length set to 0xfff
#in the decoded data below you'll see contents of memory as it reads out of bound
x.newProject()
```

    [-] Releasing the Interface
    Releasing interfaces :
    	2
    [-] Attaching the kernel driver
    Releasing interface: 0
    Releasing interface: 1
    Releasing interface: 2
    [-] Device released!
    Give your project a name?!: LeakDev
    0 : Linux 5.4.0-kali4-amd64 xhci-hcd:3:7531
    1 : Linux 5.4.0-kali4-amd64 xhci-hcd:2:7531
    2 : VIA Labs, Inc.:2071:8457
    3 : Linux 5.4.0-kali4-amd64 xhci-hcd:3:7531
    4 : Fu Rui :17201:5171
    5 : None:57506:1161
    6 : CN09357GLOG008CLA8P2A01:26403:3141
    7 : SINO WEALTH:4102:9610
    8 : VIA Technologies Inc.         :258:8457
    9 : Logitech:50475:1133
    10 : VIA Labs, Inc.:10263:8457
    11 : Linux 5.4.0-kali4-amd64 xhci-hcd:2:7531
    ---> Select a device: 4
    DEVICE ID 1433:4331 on Bus 001 Address 014 =================
     bLength                :   0x12 (18 bytes)
     bDescriptorType        :    0x1 Device
     bcdUSB                 :  0x200 USB 2.0
     bDeviceClass           :    0x0 Specified at interface
     bDeviceSubClass        :    0x0
     bDeviceProtocol        :    0x0
     bMaxPacketSize0        :   0x40 (64 bytes)
     idVendor               : 0x1433
     idProduct              : 0x4331
     bcdDevice              :  0x200 Device 2.0
     iManufacturer          :    0x1 Fu Rui 
     iProduct               :    0x2 USB Device
     iSerialNumber          :    0x3 SmartCard V4
     bNumConfigurations     :    0x1
      CONFIGURATION 1: 300 mA ==================================
       bLength              :    0x9 (9 bytes)
       bDescriptorType      :    0x2 Configuration
       wTotalLength         :   0x29 (41 bytes)
       bNumInterfaces       :    0x1
       bConfigurationValue  :    0x1
       iConfiguration       :    0x0 
       bmAttributes         :   0x80 Bus Powered
       bMaxPower            :   0x96 (300 mA)
        INTERFACE 0: Human Interface Device ====================
         bLength            :    0x9 (9 bytes)
         bDescriptorType    :    0x4 Interface
         bInterfaceNumber   :    0x0
         bAlternateSetting  :    0x0
         bNumEndpoints      :    0x2
         bInterfaceClass    :    0x3 Human Interface Device
         bInterfaceSubClass :    0x0
         bInterfaceProtocol :    0x0
         iInterface         :    0x0 
          ENDPOINT 0x82: Interrupt IN ==========================
           bLength          :    0x7 (7 bytes)
           bDescriptorType  :    0x5 Endpoint
           bEndpointAddress :   0x82 IN
           bmAttributes     :    0x3 Interrupt
           wMaxPacketSize   :   0x40 (64 bytes)
           bInterval        :   0x10
          ENDPOINT 0x3: Interrupt OUT ==========================
           bLength          :    0x7 (7 bytes)
           bDescriptorType  :    0x5 Endpoint
           bEndpointAddress :    0x3 OUT
           bmAttributes     :    0x3 Interrupt
           wMaxPacketSize   :   0x40 (64 bytes)
           bInterval        :   0x10
    do you want to detach the device from it's kernel driver: [y/n] y
    Disabling Interfaces on configuration: 1
    Disabling interfaces :
    	1
    Disabled interface: 0
    [-] Kernel driver detached
    Configuration Value: 1
    
    	Interface number: 0,Alternate Setting: 0
    
    		Endpoint Address: 0x82
    
    		Endpoint Address: 0x3
    
    Do you want to reset the device? [y/n]: n
    which Configuration would you like to use: 1
    which Interface would you like to use: 0
    which Alternate setting would you like to use: 0
    which Endpoint IN would you like to use: 0x82
    which Endpoint OUT would you like to use: 0x3
    Checking if device supports DFU mode based on USB DFU R1.1
    [32m***************************************
    * This Device doesnt support DFU mode *
    ***************************************[0m
    Do you want to claim the device interface: [y/n] y
    Checking HID report retrieval
    
    b'06a1ff0902a100857a097a150026ff007508953f8182857a097ab182857a097a9182c01201000200000040331431430002010203010902290001010080960904000002030000000921100100012223000705820340001007050303400010090229000101008096090400000203000000092110010001222300070582034000010705030340000104030904100346007500200052007500690020001603550053004200200044006500760069006300650000c4fa0000d6fa0000d80100200000000019fb00002bfb0000d8010020f6fa000019fb000054fb0000d8010020f6fa000087060784111071943052000020a3aca1a3a3a1a3baa3bf30313233343536373839b6c1bfa8b3c9b9a6d0b4caa7b0dcbac5c7ebcae4c8ebd5fdc8b7b4edcef3c9c8c7f8bcd3c3dcbde2c2ebc1acbdd3b5e7c4d4b9bac2f2b8dfb0e6b1bec9e8b1b8cafdbeddd2d1b1a3b4e6b0b4bcfcd7d4b6afc9a8c3e8d6d0d6c3c6acd3dacec8b6a8b8d0d3a6cdcbb3f6bdabbfc9d0e8b3a4c7e5bfd5c8cfcfb5cdb3b2cecad5baf3b2d9d7f7c8edbcfec8bbb3f5cabcbbafb7b5bbd8d5ecb2e2b5d8bdf8d0d000000020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020200000000052656164207375636365737321204361726420656e6372797074696f6e2e20506c65617365206d616b652065717569706d656e742075706772616465732e205468656e206465636f64652e005265616420737563636573732120497420686173206265656e207375636365737366756c6c79206465636f6465642e20507265737320746865205752495445204b657920746f2077726974652063617264732e00d4fd000000000020780200005606000090ff000078020020f83a000090b2000011131bb7420c190839046280f310271480510122c800ff0067e6096a85ae67bb72f36e3c3af54fa57f520e518c68059babd9831f19cde05b982f8a4291443771cffbc0b5a5dbb5e95bc25639f111f159a4823f92d55e1cab98aa07d8015b8312be853124c37d0c55745dbe72feb1de80a706dc9b74f19bc1c1699be48647beefc69dc10fcca10c246f2ce92daa84744adca9b05cda88f97652513e986dc631a8c82703b0c77f59bff30be0c64791a7d55163ca0667292914850ab72738211b2efc6d2c4d130d385354730a65bb0a6a762ec9c281852c7292a1e8bfa24b661aa8708b4bc2a3516cc719e892d1240699d685350ef470a06a1016c1a419086c371e4c774827b5bcb034b30c1c394aaad84e4fca9c5bf36f60232e68ee828f746f63a5781478c8840802c78cfaffbe90eb6c50a4f7a3f9bef27871c600113644b44cae8866185847a83521aa55bbbb021f08141a0353126d1261127212743a43081264122012563234237dfb1a81041a91041bbc0117012c2280321f101f465552554958494e20536d617274204361726420436f707956342e30010a420329051008051e13880820029301f473051e230168131b0a8201131c0642050000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    ..ÿ.....z.z...ÿ.u......z.z...z.z..À........3.1C..............................................................................................F.u...R.u.i.....U.S.B...D.e.v.i.c.e..Äú..Öú..Ø........û...û..Ø...öú...û..Tû..Ø...öú........q.0R..........º..0123456789.Á..³É¹.Ð.Ê..ÜºÅÇëÊäÈëÕýÈ..íÎóÉÈÇø¼ÓÃÜ½âÂëÁ.½ÓµçÄÔ¹ºÂò.ß.æ.¾Éè..Êý¾ÝÒÑ...æ..¼ü.Ô..É.ÃèÖÐÖÃÆ.ÓÚÎÈ...ÐÓ.ÍË³ö½..ÉÐè³.Çå.ÕÈÏÏµÍ³²ÎÊÕºó²Ù..Èí¼þÈ.³õÊ¼...µ.ØÕì²âµØ½øÐÐ...........................................................................................................................Read.success..Card.encryption..Please.make.equipment.upgrades..Then.decode..Read.success..It.has.been.successfully.decoded..Press.the.WRITE.Key.to.write.cards..Ôý......x...V....ÿ..x...ø....²......B...9.b.ó....Q..È.ÿ.gæ.j..g.rón..õO..R.Q.h...Ù...Íà....B.D7qÏûÀµ.Ûµé.ÂV9ñ.ñY....Õ....ª.Ø....¾.1.Ã..Ut.¾rþ.Þ...Ü.tñ.ÁÁi.ä.G¾ïÆ.Á.Ì...o.é.ª.tJÜ...Ú.ùvRQ..mÆ1.È...Ç.Y.ó.àÆG..ÕQcÊ.g.......8...üm.M..8STs.e..jv.ÉÂ...r..è..Kf..p.KÂ.QlÇ.è.Ñ...Ö.5.ôp.j..Á...l7.LwH.µ¼.4³..9JªØNOÊ..óo...hî..toc.x.xÈ...Ç.úÿ¾.ëlP...ù¾òxqÆ..6D.L..f.XG.5.ªU........S.m.a.r.t.C..d...V24..û.......¼......2...FURUIXIN.Smart.Card.CopyV4.0..B..............ôs....h........B...ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ
    [5m[34m*************************************************
    * Possible data leakage detected in HID report! *
    *************************************************[0m
    Do you want to save this device's information?[y/n]n



```python
#you can monitor the device interfaces while you are testing incase the device 
#changes its configuration when a request was sent to it or when you have interacted with the device.
x.startMonInterfaceChng()
```

    [32m********************************************
    * Interface monitoring thread has started. *
    ********************************************[0m
    [5m[34m************************************************************************************
    * 
    Device Interfaces have changed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     *
    ************************************************************************************[0m



```python
#stop monitoring for device config changes
x.stopMonInterfaceChang()
```

    [32m***********************************************
    * Monitoring of interface changes has stopped *
    ***********************************************[0m



```python

```
