import socket
from threading import Thread
import time


SERVER_PORT = 5002 # Port to open server with
SERVER_HOST = "0.0.0.0" #Server uses this as IP
separator_token = ":" #separating CLIENT from msg


client_sockets = set() #unordered set for connections later

s = socket.socket() #create socket 

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #setting options for socket to use TCP IPPROTO_TCP is option SO_REUSEADDR to reuse local addresses

s.bind((SERVER_HOST, SERVER_PORT)) #bind to socket so we can receive messages aswell.
print(f"Trying to listen server {SERVER_HOST}:{SERVER_PORT}")
s.listen(5) #wait for connection to binded server socket.


def listen_clients(client_socket):
    
    while True:
        time.sleep(1)
        try:
            #continious listening for socket
         
            message = client_socket.recv(1024).decode()
            print(message)
            message = message.replace(separator_token, ": ")
            
        except Exception as e:
            #If Exception then client no longer connected so remove it from set
            print("Error: ", e)
            client_sockets.remove(client_socket)
            break
        

        #This is for sending message to all clients
        #WIP: how to send private msg
    
           
        for client_socket in client_sockets:
            client_socket.send(message.encode())

while True:

    # Listen for new connections
    client_socket, client_address = s.accept()
    print(f" New user: {client_address} connected.")
    # add to client list.
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    
    thread = Thread(target=listen_clients, args=(client_socket,)) #create thread to listen for clients and receiveing their message. 
    # if main thread ends so do all client threads so set them as deamon since "The daemon process will continue to run as long as the main process 
    # is executing and it will terminate after finishing its execution or when the main program would be killed."
    thread.daemon = True
    # start the thread
    thread.start()
    print(client_sockets)

 
