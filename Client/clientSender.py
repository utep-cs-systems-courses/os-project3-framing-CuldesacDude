import socket
import tqdm
import os

SEPARATOR = "</>"
BUFFER_SIZE = 64 #DATA size 4096 bytes
PORT = 50000
HOST = "127.0.0.1" # ip of the client

filename2 = "Transfer file test.txt"
filename = "bakc.jpg" # test this later

#filename has to exist on the current Dir
#os.path.getsize return the size in bytes, of the file we are trying to send
filesize = os.path.getsize(filename)

currSocket = socket.socket()

print(f"¤ Connected to {HOST}:{PORT}")
currSocket.connect((HOST,PORT))
print("¤ Connected...")
print(f"{filesize}{SEPARATOR}{filename}".encode())
currSocket.send(f"{filesize}{SEPARATOR}{filename}".encode())

#begin to send file
progress = tqdm.tqdm(range(filesize),f"Sending {filename}", unit='B', unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        #read bytes
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        currSocket.sendall(bytes_read)
        progress.update(len(bytes_read))

#close socket
f.close()
currSocket.close()
