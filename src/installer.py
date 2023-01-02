'''
This code write for project Astra_store_core:
https://github.com/Reversi-Labs/Astra_store_core

Egor Bakay <egor_bakay@inbox.ru>
january 2023
'''

#from database import BD_node

class Installer:

    def __init__(self):
        self.error = {}
        self.update = {}
        self.setup = {}

    def install_program(self, install_instrucrions):
        for a in install_instrucrions:
            # make one command in console
            print(a)
        print(self.error)

    def update_all_package(self):
        pass

    def setup_package(self):
        pass

if __name__=="__main__":
    pass