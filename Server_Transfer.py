import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting for connection...")
conn, addr = s.accept()
print(addr, "has connected!")

filename = input(str("Please Enter Filename : "))
file = open (filename,'rb')
file_data = file.read()
conn.send(file_data).encode()
print("Data has been sent!")