<pre>
Done:
-Find usb and select
-parser for usbalyzer xml and searcher
-get usb device info
-create gadgetfs ( needs more cleaning )
-release the device, clean up and attach to kernel
-proxy with sniffer
-We now have a enumeration of all the interfaces and endpoints of the device we need to be able to use it
-added the clones to a flat files via json much cleaner and better ...
-- We have several hid reports now dependant on the usb device , when setting up GadgetFS ensure the user is presented with
    options to choose which hid report to be passed to the gadget.
--Setup GadgetFS method should only create a bashfile and push it to the Pi Zero and then execute it.
-- you can detaches specific interfaces  and detach each from the kernel.
-added a thread monitor to listen on interface changes
-Piped the sniff method to a pesudo terminal /dev/pts/X not to clog ipython :)
-detach the interfaces from the kernel driver inside the findselect() Method it will be better if we didnt blacklist the device driver
"""
https://stackoverflow.com/questions/23203563/pyusb-device-claimed-detach-kernel-driver-return-entity-not-found
- when coming to do the comms use Queue() so we can communicate directly to the thread
-send custom messages to the host queue



TODO:
-- add parse args to pizerorouter so you can input the max packet size currently hardcoded to 64 bytes
-send messages to device or host with ability to manipulate the payload
-fuzzer method
-replay msg or whole communication from db [ partially done but we need to work on the timing issue and threading the read portion]
-tutorial



Questions can cancelations:
-is it possible to make DMA calls (getting physical with USB Type-C) ?
-should we allow devices to be blacklisted prior to claiming them ?


   </pre>
