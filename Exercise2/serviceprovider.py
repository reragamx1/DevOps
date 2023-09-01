#!/usr/bin/python
#server socket program
""" In this program written by using TCP socket's
 communicate both single client and single server chating """
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1112
server.bind((host,port))
server.listen(10)
print ("server is listening....")
client_socket,c_addr=server.accept()
print(f"connected to {c_addr}")
while True :
    data=client_socket.recv(1024).decode()
    if not data :
        break
    print(f"client: {data}")
    message=input("server: ")
    client_socket.send(message.encode())
client_socket.close()
server.close()

