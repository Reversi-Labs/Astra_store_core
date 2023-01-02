'''
link:
https://pythonist.ru/kak-chitat-excel-fajl-xlsx-v-python/
https://codecamp.ru/blog/python-excel-tutorial/
hashmap:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

This code write for project Astra_store_core:
https://github.com/Reversi-Labs/Astra_store_core

Egor Bakay <egor_bakay@inbox.ru>
january 2023

this code need to these lib:
xlrd
xlwt
'''

import xlrd
#import xlwt
import os

class BD_install_node:

    def __init__(self,install = [],remove = []):
        self.install = install
        self.remove = remove


class BD:

    def __init__(self,path=str(os.getcwd())+"/BD.xls"):
        self.path = path
        #self.data = []
        #self.database = []
        self.setup = {}
        self.install = {}
        self.error = {}
        self.update = {}

    def print_BD(self):
        print(self.setup)
        print(self.install)
        print(self.error)
        print(self.update)

    def read_BD(self):

        def read_one_list(name_list): # workbook,
            # Load a specific sheet by name
            try: worksheet = workbook.sheet_by_name(name_list) # .sheet_by_index(i)
            except xlrd.biffh.XLRDError: return [] # end lists
            # read all list
            read = []
            a = 0
            while True:
                read.append([])
                b = 0
                try:
                    while True:
                        read[a].append(worksheet.cell(a, b).value)
                        b+=1
                except IndexError: pass
                if read[a]==[]:
                    del read[a]
                    break
                a+=1
            return read

        def unwrap_data(data,install_mode=False):
            answer = {}
            for y in range (1,len(data)):
                if data[y][0]!='': 
                    #print(data[y])
                    name = data[y][0]
                    node = 0
                    if install_mode: node = BD_install_node([data[y][1]],[data[y][2]])
                    else: node = [data[y][1]]
                    try:
                        y+=1
                        while data[y][0]=='':
                            #print(" ",data[y]) 
                            if install_mode:
                                if data[y][1]!='': node.install.append(data[y][1])
                                if data[y][2]!='': node.remove.append(data[y][2])
                            else:
                                if data[y][1]!='': node.append(data[y][1])
                            y+=1
                    except IndexError: pass
                    answer[name] = node
            return answer

        def read_list(name_list,install_mode=False):
            return unwrap_data(read_one_list(name_list),install_mode)

        # Open a workbook 
        workbook = xlrd.open_workbook(self.path)
        # read:
        self.setup   = read_list("setup")
        self.install = read_list("install",install_mode=True)
        self.error   = read_list("error")
        self.update  = read_list("update")

if __name__=="__main__":

    excel = BD()
    data = excel.read_BD()
    print("=====================")
    excel.print_BD()
