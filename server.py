from socket import *

serv = socket()

host = "localhost"
port = 7788

serv.bind((host,port))

serv.listen(3)

conn,addr = serv.accept()

print("connected to : ",addr)