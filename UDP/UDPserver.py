import socket

udpSerSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpSerSock.bind(('127.0.0.1',33333))  #绑定端口

while True:
    data, addr = udpSerSock.recvfrom(1024)
    print('data:', data.decode())
    print('addr:', addr)
    print('eval(data):', eval(data.decode()))
    udpSerSock.sendto(str(eval(data.decode())).encode('utf-8'),addr)

