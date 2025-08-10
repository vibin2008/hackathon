from PIL import Image,ImageTk
import time
import tkinter as tk
from tkinter import ttk
def logo():
    def close():
        root.destroy()

    root=tk.Tk()
    root.title("Throttlers")
    # Set geometry (widthxheight)
    root.geometry('500x500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Documents/programs/hackathon/hackathon/logo.png")
    img = img.resize((500, 500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    comp=tk.Label(root,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="white",fg="dark blue",
                  height=2,width=30)
    comp.pack()
    root.after(4000,close)
    root.mainloop()

def signin(root,tk):
    username=""
    password=""
    def clicked():
        nonlocal username,password
        username=name.get()
        password=pas.get()
        root.destroy()
    root.title("Throttlers(sign in)")
    # Set geometry (widthxheight)
    root.geometry('500x500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    name=tk.StringVar()
    pas=tk.StringVar()
    comp=tk.Label(root,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                  height=2,width=30)
    comp.pack()
    user = tk.Label(root, text = 'Username', font = ('Script MT Bold',20,'bold'),pady=20,bg="black",fg="white")
    name_entry = tk.Entry(root,textvariable = name, font=('Times new Roman',20,'normal'))
    user.pack()
    name_entry.pack()
    password=tk.Label(root,text="Password",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
    pass_entry=tk.Entry(root,textvariable=pas,font=("Times New Roman",20,"normal"))
    password.pack()
    pass_entry.pack()
    button=tk.Button(root,text="Sign In",command=clicked,font=("Cascadia Mono",20,"bold"))
    button.pack(pady=20)
    root.mainloop()
    return username,password

#getting reply from server after sign in
def signin_reply(root,tk,rep):
    root.title("Throttlers(sign in)")
    # Set geometry (widthxheight)
    root.geometry('500x500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    name=tk.StringVar()
    pas=tk.StringVar()
    comp=tk.Label(root,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                  height=2,width=30)
    comp.pack()
    user = tk.Label(root, text = 'Username', font = ('Script MT Bold',20,'bold'),pady=20,bg="black",fg="white")
    name_entry = tk.Entry(root,textvariable = name, font=('Times new Roman',20,'normal'))
    user.pack()
    name_entry.pack()
    password=tk.Label(root,text="Password",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
    pass_entry=tk.Entry(root,textvariable=pas,font=("Times New Roman",20,"normal"))
    password.pack()
    pass_entry.pack()
    reply = tk.Label(root, text=rep, font=("Times New Roman", 16, "bold"), pady=20, bg="black", fg="red")
    reply.pack(pady=20)
    root.after(3000, root.destroy)
    root.mainloop()

def sell():
    data=[]

    def clicked():
        nonlocal data
        def proceed():
            nonlocal data
            data.append(adar.get())
            data.append(typ_entry.get())
            data.append(brnd.get())
            data.append(mod.get())
            sell1.destroy()
        
        data.append(nam.get())
        data.append(phone_num.get())
        data.append(add_entry.get("1.0", tk.END))
        sell.destroy()
        sell1=tk.Tk()
        sell1.title("Throttlers")
        # Set geometry (widthxheight)
        sell1.geometry('1000x1500')

        img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
        img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
        background = ImageTk.PhotoImage(img)
        back=tk.Label(sell1,image=background)
        back.place(x=0,y=0,relwidth=1,relheight=1)
        adar=tk.StringVar()
        #typp=tk.StringVar()
        brnd=tk.StringVar()
        mod=tk.StringVar()
        comp=tk.Label(sell1,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                      height=2,width=50)
        comp.pack()
        adhar=tk.Label(sell1,text="Adhar Number",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
        adhar_entry=tk.Entry(sell1,textvariable=adar,font=("Times New Roman",20,"normal"))
        adhar.place(x=100,y=200)
        adhar_entry.place(x=400,y=210)
        typ=tk.Label(sell1,text="Vehical Type",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
        options = ["2 wheeler","4 wheeler"]
        typ_entry = ttk.Combobox(sell1, values=options, state="readonly",font=("Times New Roman",20,"bold"),width=20)

        typ.place(x=100,y=300)
        typ_entry.place(x=400,y=310)
        brand=tk.Label(sell1,text="Brand",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
        brand_entry=tk.Entry(sell1,textvariable=brnd,font=("Times New Roman",20,"normal"))
        brand.place(x=100,y=400)
        brand_entry.place(x=400,y=410)
        model=tk.Label(sell1,text="Model",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
        model_entry=tk.Entry(sell1,textvariable=mod,font=("Times New Roman",20,"normal"))
        model.place(x=100,y=500)
        model_entry.place(x=400,y=510)
        button=tk.Button(sell1,text="Proceed",command=proceed,font=("Cascadia Mono",20,"bold"))
        button.place(x=500,y=600)
        sell1.mainloop()

    
    sell=tk.Tk()
    sell.title("Throttlers")
    # Set geometry (widthxheight)
    sell.geometry('1000x1500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(sell,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    nam=tk.StringVar()
    phone_num=tk.StringVar()
    addres=tk.StringVar()
    comp=tk.Label(sell,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                  height=2,width=50)
    comp.pack()
    text = tk.Label(sell, text = 'fill in the requied details', font = ('Script MT Bold',25,'bold'),pady=20,bg="black",fg="white")
    text.pack(pady=20)
    name = tk.Label(sell, text = 'Name', font = ('Script MT Bold',20,'bold'),pady=20,bg="black",fg="white")
    name_entry = tk.Entry(sell,textvariable = nam, font=('Times new Roman',20,'normal'))
    name.place(x=100,y=300)
    name_entry.place(x=400,y=310)
    phone=tk.Label(sell,text="Phone number",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
    phone_entry=tk.Entry(sell,textvariable=phone_num,font=("Times New Roman",20,"normal"))
    phone.place(x=100,y=400)
    phone_entry.place(x=400,y=410)
    add=tk.Label(sell,text="Address",font=("Script MT Bold",20,"bold"),pady=20,bg="black",fg="white")
    add_entry = tk.Text(sell, height=5, width=30)
    add_entry.place(x=400,y=500)
    add_entry.insert(tk.END, "")
    add.place(x=100,y=500)
    button=tk.Button(sell,text="Proceed",command=clicked,font=("Cascadia Mono",20,"bold"))
    button.place(x=500,y=610)
    sell.mainloop()
    return data



def rent_sell(root,tk):
    root.title("Throttlers")
    rep=""
    def sell_rep():
        root.destroy()
        nonlocal rep
        rep="sell"
    
    def rent_rep():
        root.destroy()
        nonlocal rep
        rep="rent"
    
    # Set geometry (widthxheight)
    root.geometry('500x300')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    text = tk.Label(root, text = 'What Do you want to do?', font = ('Script MT Bold',20,'bold'),pady=20,bg="black",fg="white")
    text.pack()
    rent=tk.Button(root,text="Rent a Vehical ",command=rent_rep,font=("Times New Roman",20,"bold"))
    rent.pack(pady=20)
    sell=tk.Button(root,text="Sell a Vehical",command=sell_rep,font=("Times New Roman",20,"bold"))
    sell.pack(pady=20)
    root.mainloop()
    return rep

def case():
    val=""
    def clicked():
        nonlocal val
        value=typ_entry.get()
        op= [
    "Minor Traffic Violation",
    "Parking Violation",
    "Unpaid Traffic Fine",
    "Unpaid Parking Fine","Expired Documents (Insurance / PUC / Road Tax)",
    "Past Accident Case"]
        if value in op:
            root.destroy()
            val=value
        else:
            from tkinter import messagebox
            messagebox.showerror("Throttlers", "Your responce has been rejected due to the case registed on your vehical")
            root.destroy()
            val="case"

    root=tk.Tk()
    root.title("Throttlers")
    # Set geometry (widthxheight)
    root.geometry('500x400')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    plate=tk.StringVar()
    comp=tk.Label(root,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                  height=2,width=50)
    comp.pack()
    cas=tk.Label(root,text="enter the case",font = ('Script MT Bold',20,'bold'),pady=20,bg="black",fg="white")
    options = [
    "Minor Traffic Violation",
    "Parking Violation",
    "Unpaid Traffic Fine",
    "Unpaid Parking Fine",
    "Active Accident Case",
    "Hit-and-Run Case",
    "Theft Case",
    "Fraudulent Documents (Fake RC / Insurance / Number Plate)",
    "Expired Documents (Insurance / PUC / Road Tax)",
    "Smuggling or Illegal Transport Case",
    "Pending Court Case involving the Vehicle",
    "Manufacturer Recall (Safety Issue)",
    "Past Accident Case"]

    typ_entry = ttk.Combobox(root, values=options, state="readonly",font=("Times New Roman",20,"bold"),width=20)

    cas.pack()
    typ_entry.pack(pady=20)
    button=tk.Button(root,text="Proceed",command=clicked,font=("Cascadia Mono",20,"bold"))
    button.pack(pady=20)
    root.mainloop()
    return val


def num_plate():
    number=""
    val=""
    def clicked():
        from tkinter import messagebox
        nonlocal number
        nonlocal val
        answer = messagebox.askyesno("Vehicle Check", "Is there any case registered on this car?")
        if answer:
            number=plate.get()
            root.destroy()
            val=case()
        else:
            number=plate.get()
            root.destroy()
            val="no"
    root=tk.Tk()
    root.title("Throttlers")
    # Set geometry (widthxheight)
    root.geometry('500x400')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    plate=tk.StringVar()
    comp=tk.Label(root,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                  height=2,width=50)
    comp.pack()
    num = tk.Label(root, text = 'Reg.Number', font = ('Script MT Bold',20,'bold'),pady=20,bg="black",fg="white")
    num_entry = tk.Entry(root,textvariable = plate, font=('Times new Roman',20,'normal'))
    num.pack()
    num_entry.pack(pady=20)
    button=tk.Button(root,text="Proceed",command=clicked,font=("Cascadia Mono",20,"bold"))
    button.pack(pady=20)
    root.mainloop()
    return number,val

def four_wheeler(seat):
    root=tk.Tk()
    root.title("Throttlers")
    # Set geometry (widthxheight)
    root.geometry('1000x1500')

    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    comp=tk.Label(root,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",height=2,width=50)
    comp.pack()
    root.mainloop()


def rent():
    def four():
        def proceed():
            seat=typ_entry.get()
            four.destroy()
            four_wheeler(seat)
        root.destroy()
        four=tk.Tk()
        four.title("Throttlers")
        # Set geometry (widthxheight)
        four.geometry('500x500')
        img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
        img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
        background = ImageTk.PhotoImage(img)
        back=tk.Label(four,image=background)
        back.place(x=0,y=0,relwidth=1,relheight=1)
        comp=tk.Label(four,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                    height=2,width=50)
        comp.pack()
        que=tk.Label(four,text="How many Seats do you prefer?",font=("Script MT Bold",20,"bold"),bg="black",fg="white")
        que.pack(pady=20)
        options=['5','8','12','17']
        typ_entry = ttk.Combobox(four, values=options, state="readonly",font=("Times New Roman",20,"bold"),width=20)
        typ_entry.pack(pady=20)
        button=tk.Button(four,text="Proceed",command=proceed,font=("Times New Roman",20,"bold"))
        button.pack(pady=20)
        four.mainloop()


    root=tk.Tk()
    root.title("Throttlers")
    # Set geometry (widthxheight)
    root.geometry('500x500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    comp=tk.Label(root,text="Throttlers",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
                  height=2,width=50)
    comp.pack()
    que=tk.Label(root,text="what type of vehical do you prefer?",font=("Script MT Bold",20,"bold"),bg="black",fg="white")
    que.pack(pady=20)
    two_wheel=tk.Button(root,text="Two Wheeler",font=("Times New Roman",20,"bold"))
    two_wheel.pack(pady=20)
    four_wheel=tk.Button(root,text="Four Wheeler",command=four,font=("Times New Roman",20,"bold"))
    four_wheel.pack(pady=20)
    root.mainloop()






    



    

    
