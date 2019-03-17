import socket

s = socket.socket()
host = socket.gethostname()
port = 6667
s.bind((host, port))

s.listen(5)
while True:
    try:
        c, address = s.accept()
    except socket.error:
        break
    print('Got connection from', address)
    request = c.recv(1024)
    print(request)
    c.send(b"Thank you for connecting")
    c.close()
s.close()
