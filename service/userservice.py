from sys import path

path.insert(0,"../db/")

from dbhelper import *

table:str = "users"

def userlogin(**kwargs)->str:
	message:str = "INVALID USER"
	user:dict = getrecord(table,**kwargs)
	if user != None: message = "Successful Login"
	return message

def getalluser()->list:             return getall(table)
def updateuser(**kwargs)->bool:     return updaterecord(table,**kwargs)
def deleteuser(**kwargs)->bool:     return deleterecord(table,**kwargs)    

