import socket


def connect():
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(('localhost', 8000))
  print(client)


if __name__ == "__main__":
  connect()
