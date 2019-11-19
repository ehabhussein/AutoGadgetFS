import libagfs
from cmd import Cmd

class MyPrompt(Cmd):
        intro = 'Welcome to the AutoGFS shell.   Type help or ? to list commands.\n'
        prompt = 'Agfs> '
        agfs = libagfs.afs()

        def do_exit(self, inp):
                '''exit the application.'''
                return True

        def do_find_usb_devices(self, inp):
            '''Find and select your usb device'''
            self.agfs.findSelect()

        def do_release_device(self,inp):
            '''releases the claimed device back to its kernel driver'''
            self.agfs.releasedev()

        def do_usblyzerparse(self,inp):
            '''Parses the XML export from USBlyzer and puts it into an sqlite database\nPass a db name to it'''
            self.agfs.usblyzerparse(inp)

        def do_searchMsg(self,inp):
            '''This function allowes you to search and select messages from the db for usage'''
            self.agfs.searchmsgs()

        def do_devProxy(self,inp):
            '''will read traffic from the claimed device'''
            self.agfs.proxy(int(100))

MyPrompt().cmdloop()
 
