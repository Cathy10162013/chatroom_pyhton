
class LoginIn(State):
	"""docstring for LoginIn"""
	def __init__(self, arg):
		super(LoginIn, self).__init__()

	def display():
		while True:
			userName = inputInfo("请输入你的用户名： ")
			passWord = inputInfo("请输入你的密码: ")
			data = frame(('01',userName, passWord))
			self.tcpCliSock.send(data.encode())
        	rec = self.tcpCliSock.recv(BUFSIZE).decode() 
			if rec == '-1':
				printError("找不到用户名" + userName + "...")
				continue
			elif rec = '-2':
				printError("密码错误...")
				continue
			elif rec == '1':
				printInfo("登录成功")
				nextState
			else:
				printError("something wrong")



class LoginUp(State):
	"""docstring for LoginUp"""
	def __init__(self, arg):
		super(LoginIn, self).__init__()

	def display():
		while True:
			userName = inputInfo("请输入你的用户名： ")
			while True:
				passWord = inputInfo("请输入你的密码: ")
				if passWord == inputInfo("请再输入一遍你的密码: "):
					break;
				printError("两次输入的密码不一致")
				
			data = frame(('00', userName, passWord))
			self.tcpCliSock.send(data.encode())
        	rec = self.tcpCliSock.recv(BUFSIZE).decode() 
			if rec == '-1':
				printError("用户名" + userName + "已经存在...")
				continue
			elif rec == '1':
				printInfo("注册成功")
				nextState
			else:
				printError("something wrong")