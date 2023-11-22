from socket import *

user2 = socket()

user2.connect(("localhost",8999))

message = input("- > ")

while message != "bye":
    user2.send(message.encode())
    data = user2.recv(1024).decode()

    print(data)

    message = input("- > ")

user2.close()