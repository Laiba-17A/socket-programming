import sys
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print('failed to create socket')
    print(str(err))
    sys.exit()

print('socket created')

target_host = input('enter host name to connect: ')
target_port = input('enter target port: ')

try:
    s.connect((target_host, int(target_port)))
    print('socket connected to', target_host + ':' + target_port)
    s.shutdown(socket.SHUT_RDWR)
    s.close()
except socket.error as err:
    print('failed to connect')
    print(str(err))
    sys.exit()