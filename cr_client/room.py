from globall import*
from socket import *
		
class Room():
	"""docstring for Room"""
	def __init__(self, tcpCliSock):
		self.tcpCliSock = tcpCliSock
		self.password = 123
		self.roomNum = -1

	def startRoom(self, creator):
		self.creator = creator
		self.isPassword = (inputInfo("请输入房间密码[Y/N]: ") == 'Y')
		if self.isPassword :
			self.password = inputInfo("请输入房间密码: ")
		data = frame(('10', self.creator, self.isPassword, self.password)) 
		tcpCliSock.send(data.encode())  
		self.roomNum = tcpCliSock.recv(BUFSIZE).decode()
		if self.roomNum == -1:
			printError("something wrong...") 
		return self.roomNum
	
	def closeRoom(self, roomNum, user):
		self.isPassword = (inputInfo("请输入房间密码[Y/N]: ") == 'Y')
		if self.isPassword :
			self.password = inputInfo("请输入房间密码: ")
		data = frame('11', roomNum, user) 
		self.tcpCliSock.send(data.encode())  
		rec = self.tcpCliSock.recv(BUFSIZE).decode():
		if rec == -1:
			printError("没有关闭房间的权限或...")
		elif rec == -2:
			printError("房间不存在或者已经被关闭...")
		elif rec != 1:
			printError("something wrong")
		else:
			printInfo("成功关闭房间...")
        
	def joinRoom(self, roomNum, user):
		self.roomNum = roomNum
		data = frame('12', roomNum, user)
		rec = self.tcpCliSock.recv(BUFSIZE).decode() == -1:
		if rec == -1:
			printError("无法加入房间...")
		elif rec == -2:
			printError("房间不存在或者已经被关闭...")
		elif rec != 1:
			printError("something wrong")
		else:
			printInfo("成功加入房间...")
			printInfo("开始聊天吧！")

	def disJoinRoom(self, roomNum, user):
		self.roomNum = roomNum
		data = frame('13', roomNum, user)
		rec = self.tcpCliSock.recv(BUFSIZE).decode() == -1:
		if rec == -1:
			printError("无法退出房间...")
		elif rec == -2:
			printError("房间不存在或者已经被关闭...")
		elif rec != 1:
			printError("something wrong")
		else:
			printInfo("成功退出房间...")
			printInfo("拜拜！")

