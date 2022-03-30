import socket
import tqdm
import os

#ip
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 50001

#4096 bytes FILE SIZE
BUFFER_SIZE = 64
SEPARATOR = "</>"

#CREATE server socket
serverSocket = socket.socket()


#bind server and client
serverSocket.bind((SERVER_HOST, SERVER_PORT))

#enable server to accept connections
#number is the num of clients who can connect
serverSocket.listen(5)
print(f"¤ Listening as {SERVER_HOST}:{SERVER_PORT}")

#ACCEPT CONNECTION
client_socket , address = serverSocket.accept()
print(f"¤ {address} is connected...")
connected = True
while True:

    received = client_socket.recv(BUFFER_SIZE).decode()


    filesize, filename = received.split(SEPARATOR)
    print(f"FileSize: {filesize}, FileName: {filename}")
    #remove absolute path if any
    filename = os.path.basename(filename)
    #convert to int
    filesize = int(filesize)



    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale = True, unit_divisor=1024)
    with open(filename, "wb")as f:
        checkDataSize = 0
        while filesize > checkDataSize:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            print(f"byte_read {len(bytes_read)}")
            checkDataSize += len(bytes_read)
            if not bytes_read and filesize == checkDataSize:
                print("nothing to read")
                break
            #write to received file
            f.write(bytes_read)
            progress.update(len(bytes_read))
    if(filesize == checkDataSize):
        break

client_socket.close()
serverSocket.close()