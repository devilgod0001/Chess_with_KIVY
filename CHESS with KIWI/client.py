import socket

c = socket.socket()

c.connect(("192.168.2.206",9999))
while True:
    message = input("--->")
    c.send(bytes(message,'utf-8'))
    if message == "out":
        c.send(bytes(message,'utf-8'))
        print("Bye! Bye!")
        break
