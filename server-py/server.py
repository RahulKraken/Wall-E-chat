import socket

s = socket.socket()

PORT = 8000

s.bind(('', PORT))
print("socket binded to %s".format(PORT))

s.listen(5)
print("socket is listening for connections")

while True:
  conn, addr = s.accept()
  print(conn, addr)
