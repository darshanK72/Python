from socket import *

cli = socket()

host = "localhost"
port = 7788

cli.connect((host,port))