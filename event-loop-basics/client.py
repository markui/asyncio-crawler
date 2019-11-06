import socket
from selectors import DefaultSelector, EVENT_WRITE
import os
import subprocess



host = '172.30.97.30'
# same port number has the server
port = 9999

sock = socket.socket()
sock.setblocking(False)


def connected():
    selector.unregister(sock.fileno())
    print('connected!')

selector = DefaultSelector()
selector.register(sock.fileno(), EVENT_WRITE, connected)

try:
    sock.connect((host, port))
except BlockingIOError:
    pass


def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()
loop()