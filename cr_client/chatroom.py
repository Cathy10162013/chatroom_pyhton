
def main():
	tcpCliSock = socket(AF_INET, SOCK_STREAM)  
	tcpCliSock.connect(ADDR)  
	
	tcpCliSock.close()

if __name__ == '__main__':
	main()
	
