import socket
import threading
import random

host='127.0.0.1'
port=6000

assigned={}
used_seats=set()
lock=threading.Lock()

def handle_client(conn,addr):
    roll_no=conn.recv(1024).decode().strip()

    with lock:
        if roll_no in assigned:
            seat=assigned[roll_no]
        elif len(used_seats)>=50:
            seat=None
        else:
            seat=random.randint(1,50)
        used_seats.add(seat)
        assigned[roll_no]=seat


    if seat is None:
        conn.send('no seats available'.encode())

    else:
        conn.send(f"Your seat number is {seat}".encode())   # req 3: send to student
        print(f"Roll No: {roll_no} -> Seat: {seat}")        # req 4: display on server
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("Seating server running...")

while True:                                             # req 5: runs until stopped manually
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()