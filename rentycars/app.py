from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
def logo():
    def close():
        root.destroy()

    root=tk.Tk()
    root.title("Carowna")
    # Set geometry (widthxheight)
    root.geometry('500x500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Documents/programs/hackathon/hackathon/logo.png")
    img = img.resize((500, 500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    comp=tk.Label(root,text="Carwona",font=("Comic Sans MS",30,"bold"),bg="white",fg="dark blue",
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
    root.title("Carowna(sign in)")
    # Set geometry (widthxheight)
    root.geometry('500x500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    name=tk.StringVar()
    pas=tk.StringVar()
    comp=tk.Label(root,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
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
    root.title("Carowna(sign in)")
    # Set geometry (widthxheight)
    root.geometry('500x500')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    name=tk.StringVar()
    pas=tk.StringVar()
    comp=tk.Label(root,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
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
        sell1.title("Carowna")
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
        comp=tk.Label(sell1,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
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
    sell.title("Carowna")
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
    comp=tk.Label(sell,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
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
            messagebox.showerror("Carowna", "Your responce has been rejected due to the case registed on your vehical")
            root.destroy()
            val="case"

    root=tk.Tk()
    root.title("Carowna")
    # Set geometry (widthxheight)
    root.geometry('500x400')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    plate=tk.StringVar()
    comp=tk.Label(root,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
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
    root.title("Carowna")
    # Set geometry (widthxheight)
    root.geometry('500x400')
    img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
    img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
    background = ImageTk.PhotoImage(img)
    back=tk.Label(root,image=background)
    back.place(x=0,y=0,relwidth=1,relheight=1)
    plate=tk.StringVar()
    comp=tk.Label(root,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
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

def payment(vehicle,upi):
    import qrcode
    import tkinter as tk
    from PIL import ImageTk

    def qr(upi_id, amount, name="Carowna Rentals"):
        # Create UPI payment link
        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(upi_link)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_qr.save("payment_qr.png")

        # Show in Tkinter
        qr_window = tk.Tk()
        qr_window.title("Scan to Pay")
        qr_window.geometry("500x500")

        img_tk = ImageTk.PhotoImage(file="payment_qr.png")
        enq = tk.Label(qr_window, text ="Pay your Advance Now! \U0001F600", font = ('Times New Roman',20,'bold'))
        label = tk.Label(qr_window, text=f"Pay ₹{amount} to {name}", font=("Arial", 14,"bold"))
        enq.pack()
        label.pack(pady=10)

        qr_label = tk.Label(qr_window, image=img_tk)
        qr_label.image = img_tk
        qr_label.pack(pady=20)

        qr_window.mainloop()

    amount=vehicle[-1]*(20/100)
    qr(upi,amount, name="Carowna")

def drive(data):
    from rentycars import client
    from functools import partial
    from functools import partial
    root=tk.Tk()
    root.title("Carowna")
    # Set geometry (widthxheight)
    root.geometry('1000x1500')
    comp=tk.Label(root,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",height=2,width=50)
    comp.pack()
    canvas = tk.Canvas(root, bg="lightgray")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview,bg="black")
    # Create a frame inside the canvas
    scroll_frame = tk.Frame(canvas)
    scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    image_refs=[]
    for i in data:
        info=[]
        for j in i:
            info.append(j)
        url=info[-1]
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        image_refs.append(tk_img)
        
        name="Name: "+info[0]
        rent="Rent Per Day: "+str(info[1])
        rating="Rating: "+str(info[2])
        data=name+'\n'+rent+'\n'+rating

        car_frame = tk.Frame(scroll_frame, bg="white", bd=2, relief="groove")
        car_frame.pack(pady=10, padx=20, fill="x")

        vehicle_id=[info[1],info[-2]]
        img_label = tk.Button(car_frame, image=tk_img)
        img_label.pack(side="left", padx=10)

        # Text on the right
        text_frame = tk.Button(car_frame,text=data,bg="white",font=("Arial", 14),fg="black")
        text_frame.pack(side="left", fill="both", expand=True)



    blank=tk.Label(scroll_frame, text="", font=("Arial", 14))
    blank.pack(pady=5)    
    root.mainloop()
    


def four_wheeler(data):
    val=""
    def click(vehicle):
        def driv():
            root2.destroy()
            nonlocal val
            val="drive"
        def selfdrive(vehicle):
            def confirm(vehicle):
                root3.destroy()
                nonlocal val
                val="self"
            root2.destroy()
            root3=tk.Tk()
            root3.title("Carowna")
            # Set geometry (widthxheight)
            root3.geometry('500x400')
            img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
            img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
            background = ImageTk.PhotoImage(img)
            back=tk.Label(root3,image=background)
            back.place(x=0,y=0,relwidth=1,relheight=1)
            name="Vehicle Name: "+vehicle[0]
            price="Rent per day: "+str(vehicle[-1])
            driver="Driver: Self Drive"
            advance="Advnance Ammount: "+str(vehicle[-1]*(20/100))
            fin=name+'\n'+price+'\n'+driver
            enq = tk.Label(root3, text = fin, font = ('Times New Roman',20,'bold'),pady=20,bg="black",fg="white")
            adv = tk.Label(root3, text = advance, font = ('Times New Roman',20,'bold'),pady=20,bg="black",fg="yellow")
            conf = tk.Button(root3,text="Confirm",command=lambda: confirm(vehicle),font = ('Times New Roman',20,'bold'))
            enq.pack(pady=20)
            adv.pack()
            conf.pack(pady=20)

            root3.mainloop()

        root.destroy()
        root2=tk.Tk()
        root2.title("Carowna")
        # Set geometry (widthxheight)
        root2.geometry('500x300')
        img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
        img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
        background = ImageTk.PhotoImage(img)
        back=tk.Label(root2,image=background)
        back.place(x=0,y=0,relwidth=1,relheight=1)
        enq = tk.Label(root2, text = 'What do you prefer?', font = ('Script MT Bold',20,'bold'),pady=20,bg="black",fg="white")
        driver = tk.Button(root2,text="Driver",command=lambda: driv(),font = ('Times New Roman',20,'bold'))
        self=tk.Button(root2,text="Self Drive",command=lambda: selfdrive(vehicle),font=("Times New Roman",20,"bold"))
        enq.pack(pady=20)
        driver.pack(pady=20)
        self.pack(pady=20)
        root2.mainloop()
        
    
    
    from functools import partial
    root=tk.Tk()
    root.title("Carowna")
    # Set geometry (widthxheight)
    root.geometry('1000x1500')
    comp=tk.Label(root,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",height=2,width=50)
    comp.pack()
    canvas = tk.Canvas(root, bg="lightgray")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview,bg="black")
    # Create a frame inside the canvas
    scroll_frame = tk.Frame(canvas)
    scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    image_refs=[]
    for i in data:
        info=[]
        for j in i:
            info.append(j)
        url=info[-1]
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(img)
        image_refs.append(tk_img)
        
        name=info[1]
        data=name+'\n'
        seat="Seat:"+str(info[2])
        rent="Rent per day:"+str(info[3])
        data=data+seat+'\n'
        data=data+rent+'\n'

        car_frame = tk.Frame(scroll_frame, bg="white", bd=2, relief="groove")
        car_frame.pack(pady=10, padx=20, fill="x")

        vehicle_id=[info[1],info[-2]]
        img_label = tk.Button(car_frame, image=tk_img,command=partial(click,vehicle_id))
        img_label.pack(side="left", padx=10)

        # Text on the right
        text_frame = tk.Button(car_frame,text=data,bg="white",font=("Arial", 14),fg="black",command=partial(click,vehicle_id))
        text_frame.pack(side="left", fill="both", expand=True)



    blank=tk.Label(scroll_frame, text="", font=("Arial", 14))
    blank.pack(pady=5)    
    root.mainloop()
    return vehicle_id,val


def rent():
    seat=""
    def four():
        def proceed():
            nonlocal seat
            seat=typ_entry.get()
            four.destroy()
        root.destroy()
        four=tk.Tk()
        four.title("Carowna")
        # Set geometry (widthxheight)
        four.geometry('500x500')
        img = Image.open("C:/Users/VIBIN VIGNESH/Pictures/back.png")
        img = img.resize((1500, 1500), Image.Resampling.LANCZOS)   # LANCZOS is used to resize the image with good quality
        background = ImageTk.PhotoImage(img)
        back=tk.Label(four,image=background)
        back.place(x=0,y=0,relwidth=1,relheight=1)
        comp=tk.Label(four,text="Carowna",font=("Comic Sans MS",30,"bold"),bg="black",fg="White",
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
    return seat






    



    

    
