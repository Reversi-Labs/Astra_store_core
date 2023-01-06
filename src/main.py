'''
This code write for project Astra_store_core:
https://github.com/Reversi-Labs/Astra_store_core

Egor Bakay <egor_bakay@inbox.ru>
january 2023
'''

from database import BD
from installer import Installer

class Core(BD,Installer):

    def __init__(self):
        self.get_sudo()
        BD.__init__(self)
        self.read_BD()

if __name__=="__main__":
    test = Core()
    #test.print_BD()
    #test.setup_package()
    test.install_program(test.install["discord"].install)