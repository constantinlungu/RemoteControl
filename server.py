import socket
import time

import cv2


def save_screenshot():
    filename = time.strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    file = open(filename, 'wb')
    length = connection.recv(256).decode('UTF-8')
    length = int(length)
    i = 0
    while i <= length / 1024:
        data = connection.recv(1024)
        file.write(data)
        i += 1
    file.close()
    print("File received")
    show_screenshot(filename)


def show_screenshot(screenshot):
    img = cv2.imread(screenshot)
    cv2.imshow('Screenshot', img)
    cv2.waitKey(0)  # waits until a key is pressed
    cv2.destroyAllWindows()  # destroys the window showing image


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1234))
s.listen(0)
(connection, address) = s.accept()
print("Connected address:", address)
while True:
    command = connection.recv(256).decode("UTF-8")
    print("Received: ", command)
    if command == "ss":
        save_screenshot()
    if "exit" in command:
        break

connection.close()
print("Server closed")
