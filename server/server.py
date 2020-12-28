import socket, cv2,pickle, struct

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
port = 9999

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_address = (host_ip,port)
print('Host IP: ', host_ip)

server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("Listening at:",socket_address)

# Socket Accept
while True:
  client_socket,addr = server_socket.accept()
  print('connection from: ',addr)

  if client_socket :
    vid = cv2.VideoCapture(0)

    while(vid.isOpened()) :
      img,frame = vid.read()
      a = pickle.dumps(frame)
      message = struct.pack("Q",len(a))+a
      client_socket.sendall(message)

      cv2.imshow('Transmitting Video',frame)

      key = cv2.waitKey(1) & 0xFF
      if key == ord('q'):
        client_socket.close()
