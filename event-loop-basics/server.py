import socket
import threading

host = ''
port = 9999


def create_socket():
    try:
        global s
        s = socket.socket()
    except Exception as E:
        print(E)

def bind_socket():
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
    except Exception as E:
        print(E)

def accept_connections():
    while True:
        try:
            conn, address = s.accept()
            # s.setblocking(False)
            print(f'Connection has been established: {address}')

        except Exception as E:
            print(E)


if __name__ == '__main__':
    create_socket()
    bind_socket()
    accept_connections()
