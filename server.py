import socket
import time


def save_screenshot():
    filename = time.strftime('%Y-%m-%d %H-%M-%S') + '.png'
    file = open(filename, 'wb')
    while True:
        data = connection.recv(1024)
        if data == b'done':
            break
        file.write(data)
    file.close()
    print("File received")


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
