import socket
import time


my_socket = socket.socket()
print("Socket created successfully!")
my_socket.bind(('192.168.2.206',9999))

my_socket.listen(2)

while True:
    client, address = my_socket.accept()


    print("Connected with ", address)

    command = input("Wanna to talk?")
    if command == "yes":
        while True:
            message = client.recv(1024).decode()
            print(message)
            if message == "out":
                print("---client went offline---")
                time.sleep(3)
                break

    
    