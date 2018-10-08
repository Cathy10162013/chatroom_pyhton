BUFSIZE = 1024
HOST = '127.0.0.1'    # The remote host  
PORT = 8080                 # The same port as used by the server  
ADDR = (HOST, PORT)

def printInfo(s):
	print("\033[0;32m%s\033[0m" % s)

def printError(s):
	print("\033[0;33m%s\033[0m" % s)

def inputInfo(s):
	input("\033[0;32m%s\033[0m" % s)

# socket组帧
def frame(strlist):
	ans = ''
	for x in strlist:
		ans = ans + ','
	return ans[:,-1]

# 获得最小的没有在列表出现的数字 
def firstMinNum(xlist):
	if len(xlist)==0:
		return 1
	for i in range(len(xlist)):
		if xlist[i][0] > i+1:
			return i+1
	return len(xlist)+1

