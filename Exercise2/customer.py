#/usr/bin/python
#client socket program
""" In this program written by using TCP socket's
 communicate both single client and single server chating """
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1112
client.connect((host,port))
while True :
    message=input("client: ")
    client.send(message.encode())
    data=client.recv(1024).decode()
    print (f"server: {data}")
client.close()
