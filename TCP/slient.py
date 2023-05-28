import socket

ip_port = ('127.0.0.1',55555)
tcpSerSock = socket.socket()

# 连接
tcpSerSock.connect(ip_port)
print('输入一个数学算式(如:1+1),服务端返回计算结果')
while True:
    data = input('算式：')
    if data == '':
        continue
    data = data.encode()
    if data == 'socket_ok':
        print("socket结束！")
        break
    tcpSerSock.sendall(data)
    recv_data = tcpSerSock.recv(1024).decode()
    if recv_data != '':
        print('%s = %s'%(data.decode(),recv_data))

tcpSerSock.close()

