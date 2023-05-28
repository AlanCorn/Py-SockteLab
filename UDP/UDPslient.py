import socket

udpCliSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print('输入一个数学算式(如:1+1),服务端返回计算结果')
data = input('算式：')

udpCliSock.sendto(data.encode('utf-8'),('127.0.0.1',33333))
recv_data, addr = udpCliSock.recvfrom(1024)

print("计算结果为", recv_data.decode())

udpCliSock.close()

