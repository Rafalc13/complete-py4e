import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

header_received = False
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    if not header_received:
        print(data.decode(), end='')
        if '\r\n\r\n' in data.decode():
            header_received = True
    else:
        print(data.decode(), end='')

mysock.close()
