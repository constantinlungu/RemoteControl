import socket
import time

from mss import mss


def take_screenshot(filename):
    with mss() as sct:
        sct.shot(output=filename)
        print(filename)


def send_file(filename):
    file = open(filename, 'rb')
    data = file.read(1024)
    while data:
        s.send(data)
        data = file.read(1024)
    file.close()
    s.send(b'done')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
while True:
    command = input('command> ')
    if command == 'ss':
        s.send(bytes(command, "UTF-8"))
        timestamp = time.strftime('%Y-%m-%d %H-%M-%S') + '.png'
        take_screenshot(timestamp)
        send_file(timestamp)
