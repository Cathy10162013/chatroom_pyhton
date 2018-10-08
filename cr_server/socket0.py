# reference:
# https://www.cnblogs.com/JohnABC/p/6076006.html
# https://www.cnblogs.com/maociping/p/5132583.html

from socket import *
from select import *
class Socket():
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.bufsize = 1024
		self.addr = (host, port)

		self.tcpSerSock = socket(AF_INET, SOCK_STREAM)	# 创建套接字
		self.tcpSerSock.bind(self.addr)	# 绑定地址和端口号
		self.tcpSerSock.listen(5) # 套接字等待链接的client个数上限是5

		self.epoll_instance = epoll()
		self.epoll_instance.register(self.tcpSerSock.fileno(),EPOLLIN|EPOLLET) 
		# 注：EPOLLIN(可读)，EPOLLOUT(可写)，
		# EPOLLET: 边缘触发模式(只通知一次)，EPOLLLT：水平触发模式(通知后没有做处理的话还会继续通知)

		self.s_dict = {}	# 保存连接客户端编号的字典

	def accept(self):
		while True:
  			self.epoll_list = self.epoll_instance.poll() # 轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
  			for fd,event in self.epoll_list:
  				if fd == self.tcpSerSock.fileno():	# 如果活动socket为当前服务器socket，表示有新连接
  					cs,userinfo = self.tcpSerSock.accept()
  					self.epoll_instance.register(cs.fileno(),EPOLLIN|EPOLLET)
  					self.s_dict[cs.fileno()] = cs
  				else:
  					cs = self.s_dict[fd]
  					recv_data = cs.recv(1024)
  					print(recv_data.decode('UTF-8'))
  					if len(recv_data) > 0 :
  						cs.send(recv_data)
  					else:
  						print('adsfasdf')
  						self.epoll_instance.unregister(fd)
  						cs.close()
  						self.s_dict.pop(fd)


if __name__ == '__main__':
	socketx = Socket('127.0.0.1', 8080)
	socketx.accept()
