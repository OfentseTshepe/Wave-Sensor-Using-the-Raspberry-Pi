import socket

port =1693
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('',port))
server.listen(2)
client,address= server.accept()
while True:
    data =client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))

