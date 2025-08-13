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
        cursor.execute("update id set month='"+str(month)+"',num='"+str(1)+"' where month='"+str(rep[0])+"'")
        db.commit()
        id=id+year+month+'1'
    else:
        rep[1]=int(rep[1])
        rep[1]=rep[1]+1
        cursor.execute("update id set num='"+str(rep[1])+"' where month='"+str(rep[0])+"'")
        db.commit()
        num=str(rep[1])
        id=id+year+month+num
        print(id)
    return id

def otp(custid,otp):
    cursor.execute("insert into otp values('"+custid+"','"+str(otp)+"') ")
    db.commit()



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
    print(data) 
    tim=time.ctime()
    print(tim)
    custid=id()  
    cursor.execute("insert into sell values('"+custid+"','"+data[0]+"','"+str(data[1])+"','"+data[2]+"','"+data[3]+"','"+data[4]+"','"+data[5]+"','"+data[6]+"','"+str(tim)+"')")
    db.commit()
    print("registered succesfully!")
    return custid 

def send(data,num):
    import random
    otp=random.randint(1111,9999)
    otp_txt="OTP: "+str(otp)
    phno=data[1]
    f=open(r"C:\Users\VIBIN VIGNESH\Documents\programs\text.txt","w")
    f.write("**hello from Carowna**\n")
    f.write("your responce to sell has been recored SUCCESFULLY\n")
    f.write("Details:\n")
    text=["Name:","Phone:","Address:","Adharnumber:","Type:","Brand:","Model:"]
    for i in range(len(text)):
        text[i]=text[i]+str(data[i])
        f.write(text[i])
        f.write("\n")
    num="Register Number:"+num
    f.write(num)
    f.write("\n")
    f.write("Thank You!")
    f.close()
    import AppOpener as ap
    import keyboard as key
    f=open(r"C:\Users\VIBIN VIGNESH\Documents\programs\text.txt","r")
    a=f.readlines()
    ap.open("whatsapp")
    time.sleep(1)
    key.press_and_release("esc")
    time.sleep(1)
    key.write(str(phno))
    time.sleep(1)
    key.press_and_release("tab")
    time.sleep(2)
    key.press_and_release("enter")
    time.sleep(2)
    for i in a:
        for j in i:
            if j=="\n":
                key.press_and_release("shift+enter")
                time.sleep(1)
            else:
                key.write(j)
    key.press_and_release("shift+enter")
    time.sleep(1)
    key.write(otp_txt)
    key.press_and_release("enter")
    time.sleep(3)
    ap.close("whatsapp")
    return otp

def enter(custid,num,case):
    cursor.execute("insert into legalcase value('"+custid+"','"+num+"','"+case+"')")
    db.commit()
    print("done succesfully")

def rent(seat):
    data=[]
    cursor.execute(f"select * from {seat}")
    res=cursor.fetchall()
    for i in res:
        data.append(i)
    return data

def driver():
    data=[]
    cursor.execute(f"select * from driver")
    res=cursor.fetchall()
    for i in res:
        data.append(i)
    return data





    



