# AutoGadgetFS
Usb testing framework

Work In progress. will be documented when the project is launched


# python3 autogfs.py 

       *******************************************************************************
       *AutoGadgetFS: Automated USB testing based on gadgetfs*************************
       *******************************************************************************     
        
Welcome to the AutoGFS shell.   Type help or ? to list commands.

Agfs> help

Documented commands (type help <topic>):
========================================
devProxy  find_usb_devices  help            searchMsg    
exit      get_device_info   release_device  usblyzerparse

Agfs> help find_usb_devices\n
Find and select your usb device\n
Agfs> help searchMsg
This function allows you to search and select messages from the db for usage
Agfs> help usblyzerparse
Parses the XML export from USBlyzer and puts it into an sqlite database
Pass a db name to it
Agfs> help find_usb_devices
Find and select your usb device
Agfs> help release_device
releases the claimed device back to its kernel driver
Agfs> exit
