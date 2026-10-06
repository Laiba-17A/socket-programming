import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',6000))

name=input('enter student name: ')
client.send(name.encode())

marks=input('enter marks: ')
client.send(marks.encode())

result=client.recv(1024).decode()
print('result: ',result)

client.close()