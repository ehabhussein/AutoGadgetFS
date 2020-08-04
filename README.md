<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/agfslogos.png"/></div>

[![PayPal Donations](https://img.shields.io/static/v1?logo=Donate&label=Donate&message=To%20support%20the%20development%20of%20AGFS&color=blue)](https://www.paypal.me/autogadgetfs)

## Table of Contents

1. [What's AutoGadgetFS ?](#About)

2. [Requirments](#Requirments)

3. [The Setup](#Scenarios)

    a. [Device testing only](#Dot)
    
    b. [Minimal agfs in the middle setup](#MMITM)
    
    c. [Complete agfs in the middle setup with debugging support](#FMITM)
    
    d. [How AutoGadgetFS works](#HIW)

4. [USB Device class support](#Usbdev)

5. [Capabilities](#Caps)

6. [RoadMap](#Road)

7. [Installation](#Installation)

    a. [Linux](#Linux)

    b. [Raspberry Pi Zero with WIFI](#Rasp)
    
8. [AutogadgetFS tutorial](#Tutorial)

9. [ScreenShots](#Screens)

10. [Youtube Playlist](#Youtube)

11. [Slack](#Slack)

12. [Supported by](#Support)

13. [Buy me a coffee ☕️](#Donate)

14. [Contact me](#Contact)

---

<a name="About"/>

### What’s AutoGadgetFS ?

AutoGadgetFS is an open source framework that allows users to assess USB devices and their associated hosts/drivers/software without an in-depth knowledge of the USB protocol. The tool is written in Python3 and utilizes RabbitMQ and WiFi access to enable researchers to conduct remote USB security assessments from anywhere around the globe. By leveraging ConfigFS, AutoGadgetFS allows users to clone and emulate devices quickly, eliminating the need to dig deep into the details of each implementation. The framework also allows users to create their own fuzzers on top of it.

---

<a name="Requirments"/>

### Requirments:

* 💻 Host machine running Linux (Debian/Ubuntu/Kali)
* 🥧 Raspberry Pi Zero with WIFI support
* 🎯 Target machine options:
    * Virtual Machine
    * Standalone machine
* 🔌 2 x USB micro cables
* 🔱 Target USB device
* 🐞 Hardware debugger ( Optional )

---

<a name="Scenarios"/>

### The Setup:

<a name="Dot"/>

```bash
Device testing only:
``` 

<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/devtest.jpeg" width="450" height="187" /></div>

<a name="MMITM"/>

```bash
Minimal agfs in the middle setup:
``` 

<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/scenario1.jpeg" width="550" height="187" /></div>

<a name="FMITM"/>

```bash
Complete agfs in the middle setup with debugging support:
```

<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/scenario2.jpeg"/></div>

---

<a name="Usbdev"/>

### USB Device class support:

[✔️] USB HID Devices fully supported (Man in the middle)

[⚠️] Device only testing .. All USB devices (NO Man in the middle)

[⏳] Future releases... All USB devices (Man in the middle)

---

<a name="Caps"/>

### Capabilities:

1. Find, Select and Attach to a USB device with ease.
1. Emulate any USB HID device .
1. Perform AGFS in the middle sniffing for HID devices ( save communication to disk ).
1. Device sniffing ( Any device ).
1. Multiple Fuzzers allow you to Fuzz a device or a host.
1. Random fuzzers ( with fixed or random length packets ).
1. Smart Fuzzers that learn from previous USB communications.
1. Describe Fuzzer to tell the Fuzzer which bytes to Fuzz leaving the rest of the packet the same.
1. Gadget Fuzzer.
1. Sequential Fuzzer.
1. Control transfer Enumerator.
1. Replay of packets from a file.
1. Replay of packets from a saved USBLyzer capture.
1. Visual way of presenting packets to allow ease of reverse engineering of the communication.
1. Alerts for device in DFU mode, or if the device leaks information.
1. USB device and host can be anywhere on the internet.
1. Monitor sudden interface changes.

---

<a name="Road"/>

### RoadMap:

1. Sniff control transfer requests to a device and reply to them.
1. MITM and emulate all types of devices.
1. Console/QT based interface.
1. More Interfaces support.
1. Support more boards like the greatfet.
1. Move to a custom board.
1. Work on making raspberry pi have full support for usb device emulation with all interfaces.

---

<a name="Installation"/>

### Installation:

<a name="Linux"/>

### Linux Machine:

* Note: WSL/WSL2 is not supported due to issues with USB pass-through.

* Install Python3, ipython3 ,git, pip and rabbitMQ server

    ```bash
    sudo apt install python3 ipython3 git python3-pip rabbitmq-server dfu-util
    sudo service rabbitmq-server start
    ```

* Clone the repository

    ```bash
    git clone https://github.com/ehabhussein/AutoGadgetFS
    cd AutoGadgetFS
    ```

* Install the requirements

    ```bash
    sudo -H pip3 install -r requirements.txt
    ```

* Downgrade prompt toolkit for better ipython experience:

    ```bash
    sudo python3 -m pip install prompt-toolkit~=2.0
    ```

* Enable the web interface for rabbitMQ

    ```bash
    sudo rabbitmq-plugins enable rabbitmq_management
    http://localhost:15672/ to reach the web interface
    ```

* login to the web interface with the credentials *guest:guest*
  * NOTE: if you are not installing rabbitMQ on `localhost` add the following user and login with it:
    ```bash
    sudo rabbitmqctl add_user autogfs usb4ever
    sudo rabbitmqctl set_user_tags autogfs administrator
    ```
  * Upload the rabbitMQ configuration file
    * In the overview tab scroll to the bottom to import definitions
    * Upload the file found in: *rabbitMQbrokerconfig/rabbitmq-Config.json*

    ```bash
    sudo service rabbitmq-server restart
    ```

* Test the installation

    ```python
    sudo ipython3
    
    Python 3.7.7 (default, Apr  1 2020, 13:48:52)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.9.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: import libagfs

    In [2]: x = libagfs.agfs()

    ***************************************
    AutoGadgetFS: USB testing made easy
    ***************************************
    Enter IP address of the rabbitmq server: 127.0.0.1
  
    In [3]: exit

    sudo `python3` agfsconsole.py
    
    ***************************************
    AutoGadgetFS: USB testing made easy
    ***************************************
    Enter IP address of the rabbitmq server: 127.0.0.1
    Give your project a name?!:
   ```

* Patch Pyusb langID ( Not needed unless you get pyusb errors for langID ):
  * Edit the file `/usr/local/lib/python3/dist-packages/usb/util.py`
    * make changes to the `def get_string` method to look like below:

        ```python
        if 0 == len(langids):
            return "Error Reading langID"
            #raise ValueError("The device has no langid")
        if langid is None:
            langid = langids[0]
        elif langid not in langids:
            return "Error Reading langID"
            #raise ValueError("The device does not support the specified langid")
        ```

    * If you prefer to use `patch` apply the following patch to the file: `AutoGadgetFS/pyusb_patches/pyusb_langid.patch`

---

<a name="Rasp"/>

### Raspberry Pi Zero W:

* Obtain a copy of [Raspian Lite Edition](https://downloads.raspberrypi.org/raspios_lite_armhf_latest)
  * Burn the Image to the SD card using [BalenaEtcher](https://www.balena.io/etcher/)

* Mount the SD card on your machine and make the following changes:
  * In the `/path/to/sdcard/boot/config.txt` file add to the very end of the file:

    ```bash
    enable_uart=1
    dtoverlay=dwc2
    ```

  * In the `/path/to/sdcard/boot/cmdline.txt` add right after `rootwait`

    ```bash
    modules-load=dwc2
    ```

  * it should look like this make sure its on the same line:

    ```bash
    console=serial0,115200 console=tty1 root=PARTUUID=6c586e13-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2
    ```

* Enable ssh:
  * in the `/path/to/sdcard/boot` directory create an empty file name ssh:

    ```bash
    sudo touch /path/to/sdcard/boot/ssh
    ```

* Enable Wifi:
  * in the `/path/to/sdcard/boot` directory create an file named `wpa_supplicant.conf`:

    ```bash
    sudo vim /path/to/sdcard/boot/wpa_supplicant.conf
    ```

  * Add the following contents:

    ```bash
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US
    network={
                ssid="<your wifi SSID>"
                psk="<your wifi password>"
                key_mgmt=WPA-PSK
             }
    ```

* Unmount the SD card and place it back into the Raspberry Pi Zero and power it on.
* Copy the content of `AutogadgetFS/Pizero/` to the Pi zero: `username: pi` & `password: raspberry`

    ```bash
    cd AutogadgetFS/Pizero/
    scp gadgetfuzzer.py removegadget.sh requirements.txt router.py pi@<pi-ipaddress>:/home/pi
    ```

* SSH into the PI Zero and setup requirements for AutoGadgetFS:

    ```bash
    ssh pi@<pi-ip-address>
    chmod +x removegadget.sh
    sudo apt update
    sudo apt install python3 python3-pip
    sudo -H pip3 install -r requirements.txt
    ```
* Upgrading the latest kernel and adding modules (* This step is optional for the current release):
    ( This will take a very long time compiling on the Pi Zero, unless you choose to cross compile the kernel see [Compiling options](https://www.raspberrypi.org/documentation/linux/kernel/building.md))

    ```bash
    sudo bash
    apt install git bc bison flex libssl-dev make libncurses5-dev screen
    screen
    mkdir Downloads
    cd Downloads/
    git clone --depth=1 https://github.com/raspberrypi/linux
    cd linux/
    make bcmrpi_defconfig
    make menuconfig
    ```

    * Enable the Modules and save the config:

    <div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/allgadgets.png"/></div>
    <div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/allgadgets2.png"/></div>
    <div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/allgadgets3.png"/></div>
    <div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/allgadgets4.png"/></div>

    * Build and use the kernel:

    ```bash
    make zImage modules dtbs
    make modules_install
    cp arch/arm/boot/dts/*.dtb /boot/
    cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
    cp arch/arm/boot/dts/overlays/README /boot/overlays/
    cp arch/arm/boot/zImage /boot/kernel.img
    reboot
    ```


#### And you're done!

---

<a name="Tutorial"/>

### AutoGadgetFS tutorial:

[Click to visit the tutorial](https://docs.agfs.io/)

---

<a name="Screens"/>

### Screenshots:

##### Man in the Middle:

<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/mitm.png" /></div>

#### USB device fuzzing: 

<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/devfuzzer.png" /></div>

#### Host side fuzzing with code covereage:

<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/codecov.png" /></div>

#### Fuzzer based on a selection of bytes:

<div style="text-align:center"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/selectivefuzz.png" /></div>

#### Smart fuzzer based on learning traffic:

```python
In [44]: x.devSmartFuzz(engine="smart",samples=5,filename="/home/raindrop/PycharmProjects/AutoGadgetFs/binariesdb/Nud-Nuvoton-1046-20764-1590421333.5169587-Nuvoton-1046-20764-1590421600.8067
    ...: 274-device.bin")                                                                                                                                                                     


[+]General Statistics
Full charset                : !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
Discarded charset           : !"#$%&'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`ghijklmnopqrstuvwxyz{|}~
Final charset               : 0123456789abcdef
Word Length                 : 128
Lower Case index usage      : 92%
Lower Case index locations  : [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 121, 122, 124, 125, 127]
Upper Case index usage      : 0%
Upper Case index locations  : []
Digit index usage           : 96%
Digit index locations       : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 123, 126]
NonAN index usage           : 0%
NonAN index locations       : []
Counter statistics          : Uppercase: 0 , Lowercase: 133071, Digits:212017 , NonAlphaNumeric:0
All char Frequencies        : 
character:5 found:5012 times
character:2 found:22563 times
character:3 found:12197 times
character:8 found:15008 times
character:4 found:13275 times
character:0 found:98056 times
character:1 found:17861 times
character:f found:87823 times
character:d found:7221 times
character:7 found:9614 times
character:a found:11148 times
character:6 found:10472 times
character:b found:8189 times
character:9 found:7959 times
character:c found:9172 times
character:e found:9518 times
***********************
generated:5 Packets
***********************
Out[44]: 
['5608305852bf2ffd61770e2c827542f20be0b0fcba09db916bd07e1734b04cb0352b1d278068064d19f033bfad6fa90e53d865693fd4fee0214f00000eb0aa2c',
 '3b083595f276e2f1353a535c32f0f59516fc9328f7673bb80262c4da11c93683afe6dcff8a7a83018d78f41498a0da4d141ebd39c361b1724f2b00000eb0aa2c',
 '0120961963495c4dab9470738b497eddde07b0d70b357795ad9554d7964761969a6d997205e17eada6fa84eb33dcfb11412f75e04c195001283900000eb0aa2c',
 '091065d52127bbc6e840e02f8e1316f1c4d9c92a23931c00cdbb8c158368852ef8fabd461b98812b51ec84e1ccc5c04aaa366fbafabec623bd3500000eb0aa2c',
 '7300cc61151b7af27a578e766f49bebb2de68c48b37a00df1030ae464f456928eedd035303e697208bf58217af728a2a346fda5c8aef0335b82e00000eb0aa2c'

In [46]: x.edap.packets                                                                                                                                                                       
Out[46]: 
['5608305852bf2ffd61770e2c827542f20be0b0fcba09db916bd07e1734b04cb0352b1d278068064d19f033bfad6fa90e53d865693fd4fee0214f00000eb0aa2c',
 '3b083595f276e2f1353a535c32f0f59516fc9328f7673bb80262c4da11c93683afe6dcff8a7a83018d78f41498a0da4d141ebd39c361b1724f2b00000eb0aa2c',
 '0120961963495c4dab9470738b497eddde07b0d70b357795ad9554d7964761969a6d997205e17eada6fa84eb33dcfb11412f75e04c195001283900000eb0aa2c',
 '091065d52127bbc6e840e02f8e1316f1c4d9c92a23931c00cdbb8c158368852ef8fabd461b98812b51ec84e1ccc5c04aaa366fbafabec623bd3500000eb0aa2c',
 '7300cc61151b7af27a578e766f49bebb2de68c48b37a00df1030ae464f456928eedd035303e697208bf58217af728a2a346fda5c8aef0335b82e00000eb0aa2c']
```

#### Help method:

```python
In [15]: x.help("")                                                                                                                                                                           
Currently supported methods:
______________________________________________________________________________________________________________________________________________________________________________________________
Method               ||-->Description
----------------------------------------------------------------------------------------------------------------------------
MITMproxy            ||-->This method creates a connection to the RabbitMQ and listen on received messages on the todev queue
____________________________________________________________________________________________________________________________
MITMproxyRQueues     ||-->This method reads from the queue todev and sends the request to the device its self.
____________________________________________________________________________________________________________________________
SmartFuzz            ||-->This method is generates packets based on what it has learned from a sniff from either the host or the device
____________________________________________________________________________________________________________________________
chgIntrfs            ||-->This method allows you to change and select another interface
____________________________________________________________________________________________________________________________
clearqueues          ||-->this method clears all the queues on the rabbitMQ queues that are set up
____________________________________________________________________________________________________________________________
clonedev             ||-->This method does not need any parameters it only saves a backup of the device incase you need to share it or use it later.
____________________________________________________________________________________________________________________________
createctrltrsnfDB    ||-->creates a SQLite database containing values that were enumerated from control transfer enumeration
____________________________________________________________________________________________________________________________
createdb             ||-->create the sqlite table and columns from usblyzer captures
____________________________________________________________________________________________________________________________
decodePacketAscii    ||-->This method decodes packet bytes back to Ascii
____________________________________________________________________________________________________________________________
describeFuzz         ||-->This method allows you to describe a packet and select which bytes will be fuzzed
____________________________________________________________________________________________________________________________
devEnumCtrltrnsf     ||-->This method enumerates all possible combinations of a control transfer request
____________________________________________________________________________________________________________________________
devReset             ||-->This method Resets the device
____________________________________________________________________________________________________________________________
devWrite             ||-->To use this with a method you would write to a device make sure to run the startSniffReadThread(self,endpoint=None, pts=None, queue=None,channel=None)
____________________________________________________________________________________________________________________________
devctrltrnsf         ||-->This method allows you to send ctrl transfer requests to the target device
____________________________________________________________________________________________________________________________
deviceInfo           ||-->gets the complete info only for any usb connected to the host
____________________________________________________________________________________________________________________________
deviceInterfaces     ||-->get all interfaces and endpoints on the device
____________________________________________________________________________________________________________________________
devrandfuzz          ||-->this method allows you to create fixed or random size packets created using urandom
____________________________________________________________________________________________________________________________
devseqfuzz           ||-->This method allows you to create sequential incremented packets and send them to the device
____________________________________________________________________________________________________________________________
findSelect           ||-->This method enumerates all USB devices connected and allows you to select it as a target device as well as its endpoints
____________________________________________________________________________________________________________________________
help                 ||-->AutogadgetFS Help method
____________________________________________________________________________________________________________________________
hostwrite            ||-->This method writes packets to the host either targeting a software or a driver in control of the device
____________________________________________________________________________________________________________________________
hstrandfuzz          ||-->this method allows you to create fixed or random size packets created using urandom and send them to the host queue
____________________________________________________________________________________________________________________________
monInterfaceChng     ||-->Method in charge of monitoring interfaces for changes this is called from def startMonInterfaceChng(self)
____________________________________________________________________________________________________________________________
newProject           ||-->creates a new project name if you were testing something else
____________________________________________________________________________________________________________________________
releasedev           ||-->releases the device and re-attaches the kernel driver
____________________________________________________________________________________________________________________________
removeGadget         ||-->This method removes the gadget from the raspberryPI
____________________________________________________________________________________________________________________________
replaymsgs           ||-->This method searches the USBLyzer parsed database and give you the option replay a message or all messages from host to device
____________________________________________________________________________________________________________________________
searchmsgs           ||-->This method allows you to search and select all messages for a pattern which were saved from a USBlyzer database creation
____________________________________________________________________________________________________________________________
setupGadgetFS        ||-->setup variables for gadgetFS : Linux Only, on Raspberry Pi Zero best option
____________________________________________________________________________________________________________________________
showMessage          ||-->shows messages if error or warn or info
____________________________________________________________________________________________________________________________
sniffdevice          ||-->read the communication between the device to hosts
____________________________________________________________________________________________________________________________
startMITMusbWifi     ||-->Starts a thread to monitor the USB target Device
____________________________________________________________________________________________________________________________
startMonInterfaceChng||-->This method Allows you to monitor a device every 10 seconds in case it suddenly changes its interface configuration.
____________________________________________________________________________________________________________________________
startQueuewrite      ||-->initiates a connection to the queue to communicate with the host
____________________________________________________________________________________________________________________________
startSniffReadThread ||-->This is a thread to continuously read the replies from the device and dependent on what you pass to the method either pts or queue
____________________________________________________________________________________________________________________________
stopMITMusbWifi      ||-->Stops the man in the middle thread between the host and the device
____________________________________________________________________________________________________________________________
stopMonInterfaceChang||-->Stops the interface monitor thread
____________________________________________________________________________________________________________________________
stopQueuewrite       ||-->stop the thread incharge of communicating with the host machine
____________________________________________________________________________________________________________________________
stopSniffing         ||-->Kills the sniffing thread strted by startSniffReadThread()
____________________________________________________________________________________________________________________________
usblyzerparse        ||-->This method will parse your xml exported from usblyzer and then import them into a database
____________________________________________________________________________________________________________________________

In [16]: x.help("findSelect")                                                                                                                                                                 
****
[+]Help for findSelect Method:
[-]Signature: findSelect(self, chgint=None)


[+]findSelect Help:
This method enumerates all USB devices connected and allows you to select it as a target device as well as its endpoints
****

In [17]:                                                                                      
```

#### AutoGadgetFS console. A much simpler way to use AGFS:

<div style="text-align:left"><img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/agfsconsole.png"/></div>


---

<a name="Youtube"/>

### Youtube Playlist:

[Youtube Playlist](https://www.youtube.com/playlist?list=PLKozlVgM6RQjNHmpWR2RBiFCtufV03o6Z)

---

<a name="Slack"/>

### Join Slack:

Visit [AutogadgetFS Slack Channel](https://join.slack.com/t/autogadgetfs/shared_invite/zt-emgcv3ol-unG_axHmSQlk~5GcBddhlQ)

---

<a name="Support"/>

### Supported by:

<img src="https://pbs.twimg.com/profile_images/1039931315766870016/ahOvevDU_400x400.jpg" width="166" height="166"> <img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/JetBrains.png" width="166" height="166">  <img src="https://github.com/ehabhussein/AutoGadgetFS/raw/master/screenshots/pyusb.png" width="166" height="166"> <img src="https://i.imgur.com/r6XELEf.png" width="166" height="166">

---

<a name="Donate"/>

### Buy me a coffee to support the development of this project

[![PayPal Donations](https://img.shields.io/static/v1?logo=Donate&label=Donate&message=To%20support%20the%20development%20of%20AGFS&color=blue)](https://www.paypal.me/autogadgetfs)

---
<a name="Contact"/>

### Contact me:

### 📧: <rd@agfs.io>

### 🐦 : <https://twitter.com/0xRaindrop>
