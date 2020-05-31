#AutogadgetFS

#USB testing made easy

##Installation

####Linux machine

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

####PI zero
* Obtain a copy of [Raspian](https://www.raspberrypi.org/downloads/raspbian/)
    * Lite edition is recommended 
        * [Buster lite latest](https://downloads.raspberrypi.org/raspios_lite_armhf_latest)
    * Burn the Image to the SD card using BalenaEtcher
        * [BalenaEtcher](https://www.balena.io/etcher/)
        
<pre>
<h1>Supported by</h1>
<img src="https://github.com/ehabhussein/AutoGadgetFS/blob/master/JetBrains.png">
</pre>
