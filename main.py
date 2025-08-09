from rentycars import client
from rentycars import app
# Import Module
import tkinter as tk
from tkinter import PhotoImage
app.logo()
root=tk.Tk()
client.init()
username,password=app.signin(root,tk)
print("Throttlers")
print(username)
print(password)
a,rep=client.send(username,password)
root=tk.Tk()
app.signin_reply(root,tk,rep)
if a==str(1) or a==str(2):
    root=tk.Tk()
    rep=app.rent_sell(root,tk)
    print(rep)
    if rep=="sell":
        info=app.sell()
        num,cas=app.num_plate()
        if cas=="case":
            client.option("close")
            pass
        else:
            client.option("sell")
            print(num,cas)
            print(info)
            client.sell(info,num,cas)


client.close()
    
