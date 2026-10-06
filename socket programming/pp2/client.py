import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Enter student's ARN / roll number
arn = input("Enter your ARN: ")

# Send ARN to server
client.send(arn.encode())

# Receive assigned seat
seat = client.recv(1024).decode()

print(f"Your assigned seat number is: {seat}")

client.close()