import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 6000))
c.send(input("Enter roll number: ").encode())
print(c.recv(1024).decode())
c.close()