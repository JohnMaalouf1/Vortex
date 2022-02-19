import socket
s = socket.socket()
host = "Jacks-MacBook-Pro.local"
#input(str("Please enter the host address: "))
port = 8080
s.connect((host,port))
print("Connected")

filename = input(str("Please Enter Filename : "))
file = open (filename,'wb')
file_data = s.recv(4096)
file.write(file_data)
file.close()
print("File Received")