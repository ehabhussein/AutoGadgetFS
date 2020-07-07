import libagfs
from cmd import Cmd


class MyPrompt(Cmd):
    intro = 'Welcome to the AutoGadgetFS shell. Type help or ? to list commands.\n'
    prompt = 'AGFS> '
    agfs = libagfs.agfs()
    agfs.findSelect()

    def do_exit(self, inp):
        """exit the application."""
        return True

    def do_quit(self, inp):
        """exit the application."""
        return True

    def do_enumerate_control_transfer(self, inp):
        """Enumerate all possible combinations of control transfer requests the device supports"""
        which = input("do you want to enumerate control transfers 'fast' or 'full': ")
        if which.lower() is 'fast':
            which1 = 'fast'
        elif which.lower() is 'full':
            which1 = 'full'
        else:
            which1 = 'fast'
        self.agfs.devEnumCtrltrnsf(fuzz=which1)

    def do_new_project(self, inp):
        """create a new project"""
        self.agfs.new_project()

    def do_find_select_devices(self, inp):
        """Find and select your usb device(configuration and endpoints)"""
        self.agfs.findSelect()

    def do_release_device(self, inp):
        """releases the claimed device back to its kernel driver"""
        self.agfs.releasedev()

    def do_mitm(self, inp):
        """become man in the middle between host and device"""
        if self.agfs.device:
            dev = input("Do yo want to save the communication from host to device? [y/n]")
            if dev.lower() == 'y':
                devs = 1
            else:
                devs = 0
            hst = input("Do yo want to save the communication from device to host? [y/n]")
            if hst.lower() == 'y':
                hsts = 1
            else:
                hsts = 0
            self.agfs.startMITMusbWifi(savefile=devs, genpkts=hsts)

    def do_stopmitm(self, inp):
        """stop man in the middle sniffing"""
        self.agfs.stopMITMusbWifi()

    def do_clone(self, inp):
        """clone a selected usb device and emulate it on the raspberry pi zero"""
        self.agfs.setupGadgetFS()

    def do_unclone(self, inp):
        """Remove a gadget that is setup on the pi"""
        self.agfs.removeGadget()

    def do_clear_queues(self, inp):
        """Clear all messages in all the queues"""
        self.agfs.clearqueues()

    def do_more_help(self, inp=""):
        """Full help for each module in AutogadgetFS more useful when used as a module than this command line interface"""
        self.agfs.help(inp)

    def do_Install_steps(self):
        """show each step on how to install autogadgetfs completely"""
        pass

    def fuzzparams(self):
        howmany = int(input("How many packets do you want to generate: "))
        size = input("Size of packets do you want to generate. choose between 'fixed' and 'random': ")
        timeout = float(input("enter timeout to wait after sending each packet. (0, 0.5, 1): "))
        return howmany, size, timeout

    def do_devrandfuzz(self, inp):
        """Use this to create fixed or random size packets and send them to the device"""
        if self.agfs.device:
            howmany, size, timeout = fuzzparams()
            self.agfs.devrandfuzz(size=size, timeout=timeout)

    def do_hostrandfuzz(self, inp):
        """Use this to create fixed or random size packets and send them to the host"""
        if self.agfs.device:
            howmany, size, timeout = fuzzparams()
            self.agfs.devrandfuzz(size=size, timeout=timeout)

    def do_smartfuzzer(self, inp):
        """Generate packets based on what AGFS has learned from a sniff from either the host or the device"""
        if self.agfs.device:
            self.agfs.SmartFuzz(engine=engine, samples=samples, direction=direction, filename=filename)

    def do_change_interface(self, inp):
        """Change to another configuration of the device"""
        if self.agfs.device:
            self.agfs.chgIntrfs()

    def do_contact_me(self, inp):
        """ways to reach me"""
        print("""
### Twitter: 0XRaindrop                                     
### Email: raindrop{$}ctrl-f.org                            
### Github: https://github.com/ehabhussein                  
### Slack: https://join.slack.com/t/autogadgetfs/shared_invite/zt-emgcv3ol-unG_axHmSQlk~5GcBddhlQ 
""")


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'AGFS> '
    prompt.cmdloop()
