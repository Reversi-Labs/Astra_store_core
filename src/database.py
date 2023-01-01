'''
link:
https://pythonist.ru/kak-chitat-excel-fajl-xlsx-v-python/
https://codecamp.ru/blog/python-excel-tutorial/

This code write for project Astra_store_core:
https://github.com/Reversi-Labs/Astra_store_core

Egor Bakay <egor_bakay@inbox.ru>
january 2023

this code need to these lib:
xlrd
xlwt
'''

import xlrd
import xlwt
import os

class Excel:

    def __init__(self,path=str(os.getcwd())+"/example.xls"):
        self.path = path
        self.data = []
        self.database = []

    def read(self):
        # Open a workbook 
        workbook = xlrd.open_workbook(self.path)
        # Load a specific sheet by index 
        worksheet = workbook.sheet_by_index(0)
        # read all list
        self.data = []
        a = 0
        while True:
            self.data.append([])
            b = 0
            try:
                while True:
                    self.data[a].append(worksheet.cell(a, b).value)
                    b+=1
            except IndexError: pass
            if self.data[a]==[]:
                del self.data[a]
                break
            a+=1
        # unwrap
        self.database = self.unwrap_data()
        # end
        return self.database

    def unwrap_data(self):
        pass

if __name__=="__main__":

    #excel = test_Excel("D:/test.xls")
    #excel = Excel(str(os.getcwd())+"/example.xls")
    excel = Excel(str(os.getcwd())+"/test.xls")

    data = excel.read()
    #print(excel.get())
    for a in data:
        print(a)

    excel.write(data)

    #Excel.create_example()