# Python 3.6.1
# 参考来源（Python2）：
#    http://blog.csdn.net/qianguozheng/article/details/8497052
#    http://blog.csdn.net/chuanchuan608/article/details/17915959
# 作者：弈心逐梦 yixzm 
# 邮箱：dreamstone_xiaoqw@163.com

from socket import*  

HOST = '127.0.0.1'    # The remote host  
PORT = 8080                 # The same port as used by the server  
s = None  

def startClient():
    BUFSIZE = 1024  
    ADDR = (HOST, PORT)  


    while True:  
        data = input('> ')  
        if not data:  
            break  
        tcpCliSock = socket(AF_INET, SOCK_STREAM)  
        tcpCliSock.connect(ADDR)  
        tcpCliSock.send(data.encode())  
        data = tcpCliSock.recv(BUFSIZE).decode()  
        print(data)  
        tcpCliSock.close()  

if __name__ == "__main__":
    root = startClient()
    root.mainloop()
