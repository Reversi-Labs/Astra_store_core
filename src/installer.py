'''
This code write for project Astra_store_core:
https://github.com/Reversi-Labs/Astra_store_core

Egor Bakay <egor_bakay@inbox.ru>
january 2023
'''

# send_to_console()
import os
import sys

# for test
import time

# OC_LINUX - for test on OC windows
from sys import platform

OC_LINUX = True
if platform.upper().find("WIN")>-1: # "LINUX"
    OC_LINUX = False 

class Installer:

    def __init__(self):
        self.error = {}
        self.update = {}
        self.setup = {}

    def get_sudo(self):
        if not OC_LINUX:
            print("WARNING: root - no need because OC Windows")
            return 
        euid = os.geteuid()
        if euid != 0:
            print ("WARNING: Скрипт запущен не от root. Пробуем sudo...")
            args = ['sudo', sys.executable] + sys.argv + [os.environ]
            # Пробуем перезапустить этот скрипт (текущий процесс) через sudo.
            os.execlpe('sudo', *args)
        else:
            print ("OK: sudo")

    def install_program(self, install_instrucrions):
        for a in install_instrucrions:
            self.send_to_console(a)

    def update_all_package(self):
        for a in self.update:
            self.install_package(self.update[a])

    def setup_package(self):
        for a in self.setup:
            self.install_package(self.setup[a])

    def install_package(self,commandes):
        for comanda in commandes:
            self.send_to_console(comanda)
        print("==========================")
        print("END")

    def send_to_console(self,comanda):

        print(">>>",comanda)
        if OC_LINUX:
            a = os.popen(comanda).read()
            print(a)
        time.sleep(1)

        # добавить: если ошибка, то фиксить

if __name__=="__main__":
    test = Installer()
    test.get_sudo()