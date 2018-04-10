import socket
import time
import random

ip = '127.0.0.1'
port = 9999
sentences = ["Welcome to DS2 class", "Nice to meet you", "Hello world"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)

print "Start TCP server..."
conn, addr = s.accept()
print "Connection established"
try:
    while True:
        index = random.randint(0, 2)
        conn.send(sentences[index])
        time.sleep(1)
except:
    print "Closing the connection"
    conn.close()
