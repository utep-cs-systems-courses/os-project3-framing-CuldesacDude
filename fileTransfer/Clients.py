import socket
import threading

HEADER = 64
PORT = 5001
FORMAT = 'utf-8'
DISCONNECT = "SERVER DISCONNECTED..."
SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def comms(msg):
    data_msg = msg.encode(FORMAT)
    msg_len=len(data_msg)
    print(f"Len of msg {msg_len}")
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(data_msg)
    print(client.recv(2048).decode(FORMAT))

comms(input())
comms(DISCONNECT)