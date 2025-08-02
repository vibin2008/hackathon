import socket
import time
def init():
    global client_socket
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server (use server IP address here)
    server_ip = '192.168.29.22'  # change this to your server's IP address
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

def sell(info):
    ln=len(info)
    client_socket.send(str(ln).encode("utf-8"))
    for i in info:
        client_socket.send(i.encode("utf-8"))
        time.sleep(0.5)


def close():
    client_socket.close()
