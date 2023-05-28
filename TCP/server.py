import socket

ip_port = ('127.0.0.1',55555)       # 设置服务端地址
tcpSerSock = socket.socket()        # 用socket()方法创建socket对象
tcpSerSock.bind(ip_port)
tcpSerSock.listen(5)                # 最大连接数量为5

tcpCliSock, addr = tcpSerSock.accept()

while True:
    data = tcpCliSock.recv(1024).decode()
    print('addr:', addr)
    print('data:', data)
    if data == 'socket_ok':
        print('通信完成')
        break
    eval(data)
    print('eval(data):', eval(data))
    tcpCliSock.sendall(str(eval(data)).encode())

tcpCliSock.close()

