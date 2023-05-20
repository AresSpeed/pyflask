from mysql.connector import connect

conn:object = None
cursor:object = None

def db_connect()->object:
    return connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="student"
    )
 
def getall(table:str)->list:
    data:list = []
    sql:str = f"SELECT * FROM `{table}`"
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data

def getrecord(table:str,**kwargs)->dict: #args a list parameter to a func
    data:dict = {}
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    ##flds:str = "`=%s and `".join(keys)+"`=%s"
    sql:str = f"SELECT * FROM `{table}` WHERE `{keys[0]}`='{values[0]}'"
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    return data

def addrecord(table:str,**kwargs)->bool: #**kwargs is a list of dictionary parameters
    ok:bool = False
    values:list = list(kwargs.values())
    keys:list = list(kwargs.keys())
    fields:str = "`,`".join(keys)
    data:str = "','".join(values)

    sql:str = f"INSERT INTO `{table}`(`{fields}`) VALUES('{data}')"

    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    if cursor.rowcount>0:
        ok = True
        conn.commit() #finally write the data to the table in the db
    cursor.close()

    return ok

def updaterecord(table:str,**kwargs)->bool:
    ok:bool = False
    values:list = list(kwargs.values())
    keys:list = list(kwargs.keys())
    flds:list = []
    for i in range(1,len(values)):
        flds.append("`"+keys[i]+"`='"+values[i]+"'")
    fields:str = ",".join(flds)
    sql:str = f"UPDATE `{table}` SET {fields} WHERE `idno` = '{values[1]}'" 

    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    if cursor.rowcount>0:
        ok = True
        conn.commit() #finally write the data to the table in the db
    cursor.close()
    return ok

def deleterecord(table:str,**kwargs)->bool:
    ok:bool = False
    keys:list = list(kwargs.keys())
    values:list = list(kwargs.values())
    
    sql:str = f"DELETE FROM `{table}` WHERE `{keys[0]}` ='{values[0]}'"
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    if cursor.rowcount>0:
        ok = True
        conn.commit()
    cursor.close()
    return ok

def loginrecord(table, **kwargs)->bool:
    message = "INVALID USER!"
    values = list(kwargs.values())
    sql = f"SELECT * FROM `{table}` WHERE `username`=%s AND `password`=%s"
    
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql,values)
    data = cursor.fetchone()
    cursor.close()
    if data: message = "LOGIN ACCEPTED"
    return message
    
"""
    conn = db_connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `users` WHERE `username`=%s AND `password`=%s", (username, password))
    data = cursor.fetchone()
    cursor.close()
    return data
"""
def main()->None:
    ok:bool = getall('student')
    print(ok)

if __name__ == "__main__":
    main()