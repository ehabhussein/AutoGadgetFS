# AutogadgetFS
# USB testing made easy
## Installation
#### Linux machine

* Install Python3.7, ipython3 ,git, pip and rabbitMQ server
    * ```$ sudo apt install python3.7 ipython3 git python3-pip rabbitmq-server```
    * ```$ sudo service rabbitmq-server start```
* Clone the repository
    * ```$ git clone https://github.com/ehabhussein/AutoGadgetFS```
    * ```$ cd AutoGadgetFS```
        * Install the requirements
            * ```$ sudo -H pip3 install -r requirements.txt```
            * ```$ sudo -H pip3 install cmd```
* Enable the web interface for rabbitMQ
    * ```$ sudo rabbitmq-plugins enable rabbitmq_management```    
    * ```http://localhost:15672/ to reach the web interface```
        * login to the web interface with the credentials *guest:guest*
            * Upload the rabbitMQ configuration file
                * In the overview tab scroll to the bottom to import definitions
                * Upload the file found in: *rabbitMQbrokerconfig/rabbitmq-Config.json*
    * ```$ sudo service rabbitmq-server restart```
* Test the installation 
    ```
    $ sudo ipython3
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
    
    $ sudo python3.7 agfsconsole.py
    ***************************************
    AutoGadgetFS: USB testing made easy
    ***************************************
    Enter IP address of the rabbitmq server: 127.0.0.1
    Give your project a name?!: 
   ```
* Patch Pyusb langID:
    * Edit the file */usr/local/lib/python3.7/dist-packages/usb/util.py*
        * make changes to the *def get_string* method to look like below:
        ```
        if 0 == len(langids):
            return "Error Reading langID"
            #raise ValueError("The device has no langid")
        if langid is None:
            langid = langids[0]
        elif langid not in langids:
            return "Error Reading langID"
            #raise ValueError("The device does not support the specified langid")
        ```
    * If you prefer to use *patch* apply the following patch to the file:
        * AutoGadgetFS/pyusb_patches/pyusb_langid.patch

#### PI zero
* Obtain a copy of [Raspian](https://www.raspberrypi.org/downloads/raspbian/)
    * Lite edition is recommended 
        * [Buster lite latest](https://downloads.raspberrypi.org/raspios_lite_armhf_latest)
    * Burn the Image to the SD card using BalenaEtcher
        * [BalenaEtcher](https://www.balena.io/etcher/)
* Mount the SD card on your machine and make the following changes:
    * In the */path/to/sdcard/boot/config.txt* file add to the very end of the file:
        ```
        enable_uart=1
        dtoverlay=dwc2
        ```
    * In the */path/to/sdcard/boot/cmdline.txt* add right after *rootwait* 
        ```
        modules-load=dwc2
        ```
        * it should look like this make sure its on the same line:
        ```
      console=serial0,115200 console=tty1 root=PARTUUID=6c586e13-02 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2
      ```
* Enable ssh:
    * in the */path/to/sdcard/boot* directory create an empty file name ssh:
        ```
        $ sudo touch /path/to/sdcard/boot/ssh
       ```
* Enable Wifi:
    * in the */path/to/sdcard/boot* directory create an file named *wpa_supplicant.conf*:
        ```
        $ sudo vim /path/to/sdcard/boot/wpa_supplicant.conf
        ```
        * Add the following contents:
            ```ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
                update_config=1
                country=US
                network={
                    ssid="<your wifi SSID>"
                    psk="<your wifi password>"
                    key_mgmt=WPA-PSK
                }
          ``` 
* Unmount the SD card and place it back into the Raspberry Pi Zero and power it on.
* Copy the content of *AutogadgetFS/Pizero/* to the Pi zero: *username: pi / password: raspberry*
    ```
    $ cd AutogadgetFS/Pizero/
    $ scp gadgetfuzzer.py removegadget.sh requirements.txt router.py pi@<pi-ipaddress>:/home/pi
    ``` 
* SSH into the PI Zero and setup requirements for AutoGadgetFS:
    ```
    $ ssh pi@<pi-ip-address>
    $ chmod +x removegadget.sh
    $ sudo apt update
    $ sudo apt install python3.7 python3-pip
    $ sudo -H pip3 install -r requirements.txt
    ```
# And you're done!

<pre>	
<h1>Supported by</h1>	
<img src="https://github.com/ehabhussein/AutoGadgetFS/blob/master/JetBrains.png">	
</pre>
