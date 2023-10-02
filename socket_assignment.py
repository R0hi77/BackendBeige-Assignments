import socket # socket module
import configparser

'''
server script that binds a port and responds to connections
script by : Nana Kwadwo and Petersburg
 
'''

#configuration file path
beigefilepath ="cohort1.txt"

#create a socket
# AF_INET - IPv4 address family, SOCK_STREAM-  - TCP protocol
s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created sucessfully")

# read the configuration file
config = configparser.ConfigParser()
config.read(open(beigefilepath)) 

#port number and host ip
host = '127.0.0.1' 
port = 5000
server_address =  (host, port)

# binding the socket to server address (ip, port
s.bind(server_address) 

#listening  for connections 
s.listen() 

#accepts connections
(comm_socket, address) = s.accept()

while True:
    try:
       
        print(f"Got a connection from {comm_socket}")
        comm_socket.send(b"connected to the server\n")
     
        # reaciving user input
        comm_socket.send(b"Enter string :")
        data = comm_socket.recv(1024).decode('utf-8').strip()

        # comparing user input to the config file content
        with open(beigefilepath,mode='r')  as configfile:
            if data + '\n' in configfile.readlines():
                response ="STRING FOUND\n"
                #print(response)
            else:
                response = "STRING NOT FOUND\n"
                #print(response)

        comm_socket.sendall(response.encode('utf-8'))
    finally:
        #comm_socket.close()
        print("should loop back\n")

