import asyncio
import websocket

from threading import Thread
from time import sleep

def on_message(ws, msg):
  print(f"> {msg}")

def on_error(ws, error):
  print(f"> {error}")

def on_close(ws):
  print("--- Connection closed ---")

def run(ws):
  while True:
    name = input()
    ws.send(name)

def on_open(ws):
  print("Connection opened")
  thread = Thread(target=run, args=(ws, ))
  thread.start()
  print("Thread running")

if __name__ == "__main__":
  websocket.enableTrace(True)
  ws = websocket.WebSocketApp(
    "ws://localhost:8080/ws",
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
  )
  ws.on_open = on_open
  ws.run_forever()
