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
            self.send_to_console(a)

    def update_all_package(self):
        for a in self.update:
            commandes = self.setup[a]
            for comanda in commandes:
                self.send_to_console(comanda)

    def setup_package(self):
        for a in self.setup:
            commandes = self.setup[a]
            for comanda in commandes:
                self.send_to_console(comanda)

    def send_to_console(self,data):
        print(">>>",data)
        # добавить: если ошибка, то фиксить

if __name__=="__main__":
    pass