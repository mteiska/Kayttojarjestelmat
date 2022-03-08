from email import message_from_string
from threading import Thread
import socket

# server's IP address

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 # server's port
separator_token = ":" # Separator for name and msg
# Ask client for nickname
nickname = input("Enter your name: ")

# Create the TCP Socket for client
s = socket.socket()
print(f"Trying to connect to:  {SERVER_HOST}:{SERVER_PORT}")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("Connection succesful.")


def message_listener():
    while True:
        message = s.recv(1024).decode()
       
        print("\n" + message)


# make a thread that listens for messages to this client & print them
t = Thread(target=message_listener)
# Again lets create daemon thread so it ends when main process ends according to same principle used in server side.
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    msg_to_send =  input()
    # a way to exit the program
    if msg_to_send.lower() == 'disconnect':
        break
   
    
    to_send = f"{nickname}{separator_token}{msg_to_send}" #send
    # finally, send the message
    s.send(to_send.encode())

s.close()  # close socket once 'disconnect' message has been send.
