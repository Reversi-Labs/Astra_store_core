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

class BD_node:

    def __init__(self,install = [],remove = []):
        self.install = install
        self.remove = remove


class Excel:

    def __init__(self,path=str(os.getcwd())+"/BD.xls"):
        self.path = path
        #self.data = []
        #self.database = []
        self.setup = {}
        self.install = {}
        self.error = {}

    def read(self):
        # Open a workbook 
        workbook = xlrd.open_workbook(self.path)
        # read INSTALL instructions:
        for i in range(3):
            # Load a specific sheet by index 
            worksheet = workbook.sheet_by_index(i)
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
            # unwrap
            if   i==0: self.setup   = self.unwrap_install(read)
            elif i==1: self.install = self.unwrap_install(read)
            else:      self.error   = self.unwrap_install(read,error_mode=True)
            # end
        #return self.database

    def unwrap_install(self,data,error_mode=False):
        answer = {}
        for y in range (1,len(data)):
            if data[y][0]!='': 
                #print(data[y])
                name = data[y][0]
                node = 0
                if error_mode: node = [data[y][1]]
                else: node = BD_node([data[y][1]],[data[y][2]])
                try:
                    y+=1
                    while data[y][0]=='':
                        #print(" ",data[y]) 
                        if error_mode:
                            if data[y][1]!='': node.append(data[y][1])
                        else:
                            if data[y][1]!='': node.install.append(data[y][1])
                            if data[y][2]!='': node.remove.append(data[y][2])
                        y+=1
                except IndexError: pass
                answer[name] = node
        return answer

if __name__=="__main__":

    excel = Excel()

    data = excel.read()
    #print(excel.get())
    # for a in data:
    #     print(a)

    # hashmap = {'jack': 4098, 'sape': 4139}
    # print(hashmap)
    # hashmap['guido'] = 4127
    # print(hashmap)

    print("=====================")
    print(excel.setup)
    print(excel.install)
    print(excel.error)
