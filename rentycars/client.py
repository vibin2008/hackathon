import socket
import time
import pickle
def init():
    global client_socket
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server (use server IP address here)
    server_ip = '192.168.1.107'  # change this to your server's IP address
    server_port = 8080

    client_socket.connect((server_ip, server_port))
    print("connected to server!")

def send(username,password):
    # Create a socket object
    client_socket.send(username.encode("utf-8"))
    client_socket.send(password.encode("utf-8"))

    #reciving reply from server
    a=client_socket.recv(1024).decode("utf-8")
    rep=client_socket.recv(1024).decode("utf-8")
    return a,rep

    # Close the socket
def option(op):
    client_socket.send(op.encode("utf-8"))

def sell(info,num,cas):
    ln=len(info)
    client_socket.send(str(ln).encode("utf-8"))
    time.sleep(0.5)
    for i in info:
        client_socket.send(i.encode("utf-8"))
        time.sleep(0.5)
    client_socket.send(num.encode("utf-8"))
    client_socket.send(cas.encode("utf-8"))

def rent(seat):
    client_socket.send(seat.encode("utf-8"))
    #data=client_socket.recv(1024).decode("utf-8")
    data = client_socket.recv(4096)
    data = pickle.loads(data)
    return data

def driv(info):
    client_socket.send(info.encode("utf-8"))
    data = client_socket.recv(4096)
    data = pickle.loads(data)
    return data

def upi():
    info="upi"
    client_socket.send(info.encode("utf-8"))
    rep=client_socket.recv(1024).decode("utf-8")
    return rep




    


def close():
    client_socket.close()
