from sys import path

path.insert(0,"../db/")

from dbhelper import *

table:str = "student"

def getallstudent()->list:           return getall(table)
def getstudent(**kwargs)->list:      return getrecord(table,**kwargs)
def addstudent(**kwargs)->list:      return addrecord(table,**kwargs)
def updatestudent(**kwargs)->list:   return updaterecord(table,**kwargs)
def deletestudent(**kwargs)->list:   return deleterecord(table,**kwargs)

"""
def main()->None:
    print(deletestudent(idno='0009'))
    
    
if __name__=="__main__":
    main()
"""



