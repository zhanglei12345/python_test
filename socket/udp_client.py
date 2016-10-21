import socket
from datetime import datetime

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#addr = ('127.0.0.1', 10021)       #服务器端地址
#while True:
#    data = input('请输入要处理的数据:') #获得数据
#    if not data or data == 'quit':
#        break
#    s.sendto(data.encode(), addr)    #发送到服务端
#    recvdata, addr = s.recvfrom(1024)  #接收服务器端发来的数据
#    print(recvdata.decode('utf-8'))    #解码打印

server_address = ('localhost',9999)
max_size = 4096

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey!',server_address)
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said',data)

client.close()            #关闭socket
