import socket

HOST = "127.0.0.1"
PORT = 5000

# Keep track of assigned seats
assigned_seats = set()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started...")
print("Waiting for student connections...")

while True:
    conn, addr = server.accept()

    print(f"\nStudent connected: {addr}")

    # Receive student's roll/ARN
    arn = conn.recv(1024).decode()

    # Find an available seat
    if len(assigned_seats) < 50:
        for seat in range(1, 51):
            if seat not in assigned_seats:
                assigned_seats.add(seat)
                break

        # Send seat number to student
        conn.send(str(seat).encode())

        # Display on server
        print(f"Student Roll Number: {arn}")
        print(f"Assigned Seat Number: {seat}")

    else:
        conn.send("No seats available".encode())
        print("All 50 seats have been assigned.")

    conn.close()