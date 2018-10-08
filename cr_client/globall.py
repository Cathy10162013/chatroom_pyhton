# referance: https://www.cnblogs.com/hellojesson/p/5961570.html

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

def frame(strlist):
	ans = ''
	for x in strlist:
		ans = ans + ','
	return ans[:,-1]