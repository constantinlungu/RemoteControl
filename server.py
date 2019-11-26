import socket

import cv2
import numpy as np


def save_screenshot():
    length = connection.recv(256).decode('UTF-8')
    connection.send("Length received".encode())
    length = int(length)
    i = 0
    data = b''
    while i <= length / 1024:
        data += connection.recv(1024)
        i += 1
    print("File received")
    decoded_screenshot = cv2.imdecode(np.frombuffer(data, np.uint8), -1)
    show_screenshot(decoded_screenshot)
    connection.send("Image received".encode())


def show_screenshot(screenshot):
    cv2.imshow('Screenshot', screenshot)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1234))
s.listen(0)
(connection, address) = s.accept()
print("Connected address:", address)
while True:
    command = connection.recv(256).decode("UTF-8")
    print("Received: ", command)
    if command == "ss":
        while True:
            save_screenshot()
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    if "exit" in command:
        break

connection.close()
print("Server closed")
