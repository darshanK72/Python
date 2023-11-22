from socket import *

user1 = socket()

user1.bind(("localhost",8999))

user1.listen(1)

conn, addr = user1.accept()

print("Connected to User2 :",addr)

data = conn.recv(1024).decode()

while True:
    if not data:
        break
    print(data)

    message = input("- > ")

    conn.send(message.encode())

    data = conn.recv(1024).decode()

conn.close()