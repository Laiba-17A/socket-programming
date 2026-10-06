import socket
import threading

host='127.0.0.1'
port=6000
lock=threading.Lock()

def handle_client(conn,addr):
    print('connected: ',addr)

    name=conn.recv(1024).decode()

    marks=int(conn.recv(1024).decode())

    if marks>=50:
        result='pass'
    else:
        result='fail'

    with lock:
        with open('result.txt','a') as f:
            f.write(name + ", " + str(marks) + ", " + result + "\n")

    conn.send(result.encode())
    conn.close()
    print('disconnected: ',addr)


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print('server listening on ',host,port)

while True:
    conn,addr=server.accept()
    t=threading.Thread(target=handle_client,args=(conn,addr))
    t.start()