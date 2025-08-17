import socket
import pickle
import time
from rentycars import database
def option():
    message = conn.recv(1024).decode("utf-8")
    return message

def sell():
    data=[]
    ln = conn.recv(1024).decode("utf-8")
    ln=int(ln)
    for i in range(ln):
        info = conn.recv(1024).decode("utf-8")
        data.append(info)
    num=conn.recv(1024).decode("utf-8")
    case=conn.recv(1024).decode("utf-8")
    return data,num,case



data=[]

# Create a socket object
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
server_socket.bind(('192.168.1.107', 8080)) 

# Start listening

server_socket.listen(1)
print("Server is listening for connections...")

# Accept a connection
conn, addr = server_socket.accept()

# Receive message
for i in range(2):
    message = conn.recv(1024).decode("utf-8")
    data.append(message)
print("message recived")

a,rep=database.signin(data[0],data[1])
#sending reply to client
conn.send(a.encode("utf-8"))
conn.send(rep.encode("utf-8"))

def driv(info):
    
    print(seat)


op=option()
if op=="sell":
    data,num,case=sell()
    custid=database.sell(data)
    database.enter(custid,num,case)
    otp=database.send(data,num)
    database.otp(custid,otp)

elif op=="rent":
    seat = conn.recv(1024).decode("utf-8")
    seat = seat+"seater"
    data=database.rent(seat)
    #conn.send(str(data).encode("utf-8"))
    conn.sendall(pickle.dumps(data))
    time.sleep(5)
    info = conn.recv(1024).decode("utf-8")
    if info=="driver":
        data=database.driver()
        conn.sendall(pickle.dumps(data))
    elif info=="upi":
        upi="shreebhavankaarthik@oksbi"
        conn.send(upi.encode("utf-8"))

elif op=="close":
    pass





# Close connection
conn.close()




