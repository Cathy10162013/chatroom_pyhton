# https://www.cnblogs.com/PrettyTom/p/6626229.html

from socket import *
from select import *

s = socket(2,1)
s.setsockopt(1,2,1)
s.bind(('127.0.0.1',8080))
s.listen(1024)

s_dict = {}

epoll_instance = epoll()
epoll_instance.register(s.fileno(),EPOLLIN|EPOLLET)
while 1:
    epoll_list = epoll_instance.poll()
    for fd,event in epoll_list:
        if fd == s.fileno():
            cs,userinfo = s.accept()
            epoll_instance.register(cs.fileno(),EPOLLIN|EPOLLET)
            s_dict[cs.fileno()] = cs
        else:
            cs = s_dict[fd]
            recv_data = cs.recv(1024)
            print(recv_data.decode('gb2312'))
            if len(recv_data) > 0 :
                cs.send(recv_data)
            else:
                print('adsfasdf')
                epoll_instance.unregister(fd)
                cs.close()
                s_dict.pop(fd)