import socket

# Create a TCP socket
# AF_INET = IPv4
# SOCK_STREAM = TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP address and port number
HOST = '127.0.0.1'
PORT = 5000

# Bind the socket to the IP address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming client connections
# 5 means maximum number of waiting connections
server_socket.listen(5)

print("Server is waiting for a connection...")

# Accept a client connection
# conn = new socket used to communicate with the client
# addr = client's IP address and port
conn, addr = server_socket.accept()

print("Client connected:", addr)

# Receive data from the client
# 1024 = maximum number of bytes to receive
data = conn.recv(1024).decode()

print("Message from client:", data)

# Send a response back to the client
message = "Hello from Server!"
conn.send(message.encode())

# Close the connection with the client
conn.close()

# Close the server socket
server_socket.close()

print("Server closed.")
