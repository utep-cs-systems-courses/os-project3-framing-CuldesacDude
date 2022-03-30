import socket
import threading
import io

PORT = 5001
#ONLY 64 BITS of transfer data
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS=(SERVER,PORT)
#utf-8 reads and writes unicode files
FORMAT = 'utf-8'
DISCONNECT = "SERVER HAS DISCONNECTED."

#AF_INET address family ipv4 type of protocol ?
#use SOCK_STREAM for data streaming
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def client_manager(connection, address):
    print(f"CURRENT CONNECTION: {address}")
    connected = True

    while connected:
        msg_len = connection.recv(HEADER).decode(FORMAT)

        if msg_len:
            #size of msg
            msg_len = int(msg_len)
            print(f"int msg size {msg_len}")
            #data string stream
            msg = connection.recv(msg_len).decode(FORMAT)
            #check if server and client are connected.
            if msg == DISCONNECT:
                connected = False
            print(f"[{address}], {msg}")
            connection.send("MSG RECEIVED".encode(FORMAT))
        #Close SERVER
    connection.close()

def init_Server():
    server.listen()
    print(f"LISTENING to {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=client_manager, args=(connection,address))
        thread.start()
        #print(f"[ACTION CONNECTIONS]{threading.active_count()-1}")

print("Starting...")
init_Server()