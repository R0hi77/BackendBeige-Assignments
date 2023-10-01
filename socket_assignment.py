import socket # socket module
import configparser
import threading

''' script binds to a port and responds to a connection '''

def handle_client(ip,port):
    print(f"Got connection from {ip}") 
    ip.send(b"You have connected")
    ip.close()


#configuration file path
beigefilepath ="cohort1.txt"

#create a socket
# AF_INET - IPv4 address family, SOCK_STREAM-  - TCP protocol
s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created sucessfully")

# read the configuration file
config = configparser.ConfigParser()
config.read(beigefilepath) 

#port number and host ip
host = '127.0.0.1' 
port = 5000
server_address =  (host, port)

# binding the socket to server address (ip, port
s.bind(server_address) 

#listening connections 
s.listen() 


while True:
    (comm_socket, address) = s.accept()

    try:

        t=threading.Thread(target=handle_client,args=(comm_socket,address))

        t.start()

        data = comm_socket.recv(1024).decode('utf-8').strip()

        with open(beigefilepath,mode='r')  as configfile:
            if data + '\n' in configfile.readlines():
                response ="STRING FOUND"
                print(response)
            else:
                response = "STRING NOT FOUND"
                print(response)

        comm_socket.sendall(response.encode('utf-8'))
    finally:
        comm_socket.close()
