import socket

# Create TCP socket
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Server address
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000

# Connect to server
client_socket.connect(
    (SERVER_IP, SERVER_PORT)
)

print("Connected to server.")

while True:

    # Take input from user
    message = input("Enter message: ")

    # Exit condition
    if message.lower() == "exit":
        break

    # Send message to server
    client_socket.send(message.encode())

    # Receive server response
    response = client_socket.recv(1024).decode()

    print("Server:", response)

# Close connection
client_socket.close()

print("Client disconnected.")