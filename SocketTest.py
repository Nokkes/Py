import socket
port = 5901
host = '192.168.0.128'
sock = socket.socket()
tst = sock.connect((host, port))


print (tst)