import mysql.connector as mysql
import time
global db
global cursor
# Establish the connection
db = mysql.connect(
    host="localhost",       # Replace with your MySQL server host
    user="root",   # Replace with your MySQL username
    password="Vibin@#123",
    database="rentycars"
    )

 #creating cursor
cursor=db.cursor()

def id():
    rep=[]
    from datetime import datetime
    id="CUST"
    now=datetime.now()
    year=now.strftime("%y")
    month=now.strftime("%m")
    cursor.execute("select * from id")
    res=cursor.fetchall()
    for i in res:
        for j in i:
            rep.append(j)
    if str(rep[0])!=month:
        cursor.execute("update id set month='"+month+"' and num=1 where month='"+str(rep[0])+"'")
        id=id+year+month+'1'
    else:
        cursor.execute("update id set num='"+str(rep[1]+1)+"' where month='"+str(rep[0])+"'")
        num=str(rep[1]+1)
        id=id+year+month+num
    return id


def signin(u,p):
    rep=[]
    cursor.execute("select * from signin where username= '"+u+"' ")
    res=cursor.fetchall()
    for i in res:
        for j in i:
            rep.append(j)
    if rep==[]:
        cursor.execute("insert into signin values('"+u+"','"+p+"') ")
        db.commit()
        a='1'
        return a,"new signin registered!"
    elif rep[0]==u and rep[1]==p:
        a='2'
        return a,"signed in succesfully!"

    elif rep[0]==u and rep[1]!=p:
        a='0'
        return a,"wrong password, \n if you are a new user the username is not avilable!"

def sell(data): 
    tim=time.ctime()
    custid=id()  
    cursor.execute("insert into sell values('"+custid+"','"+data[0]+"','"+str(data[1])+"','"+data[2]+"','"+data[3]+"','"+data[4]+"','"+data[5]+"','"+data[6]+"','"+str(tim)+"'")")
    print("registered succesfully!")   

    



