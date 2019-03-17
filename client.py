import socket

s = socket.socket()
host = socket.gethostname()
port = 6667

s.connect((host, port))
s.send(b"Hello from client!")
print(s.recv(1024))
s.close()
