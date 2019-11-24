import socket

import mss
import mss.tools


def take_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        image = sct.grab(monitor)
        return mss.tools.to_png(image.rgb, image.size)


def send_screenshot(screenshot):
    print(len(raw_bytes))
    image_size = len(raw_bytes)
    s.send(str(image_size).encode())
    s.sendall(screenshot)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
while True:
    command = input('command> ')
    if command == 'ss':
        s.send(bytes(command, "UTF-8"))
        raw_bytes = take_screenshot()
        send_screenshot(raw_bytes)
