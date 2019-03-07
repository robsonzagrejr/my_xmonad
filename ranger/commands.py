# This is a sample commands.py.  You can add your own commands here.
#
# Please refer to commands_full.py for all the default commands and a complete
# documentation.  Do NOT add them all here, or you may end up with defunct
# commands when upgrading ranger.

# A simple command for demonstration purposes follows.
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# You can import any python module as needed.
import os

# You always need to import ranger.api.commands here to get the Command class:
from ranger.api.commands import Command


# Any class that is a subclass of "Command" will be integrated into ranger as a
# command.  Try typing ":my_edit<ENTER>" in ranger!
class mount(Command):
    def execute(self):
        import subprocess
        import time
        subprocess.Popen("udiskie",shell=True)
        time.sleep(1)
        subprocess.Popen("pkill udiskie",shell=True)
        subprocess.call("clear",shell=True)
        subprocess.call("ranger",shell=True)
        #self.fm.notify(self.fm.thisfile.path)

class umount(Command):
    def execute(self):
        import subprocess
        import time
        aux = "udiskie-umount --detach "+self.fm.thisfile.path
        subprocess.Popen(aux,shell=True)
        time.sleep(1)
        subprocess.call("clear",shell=True)
        subprocess.call("ranger",shell=True)

class playlist(Command):
    def execute(self):
        from os import system
        system("find -type f -iname \*.m\* > "+self.fm.thisdir.basename+".playlist")
        
