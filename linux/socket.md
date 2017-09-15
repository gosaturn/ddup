> [socket详细介绍](https://www.cnblogs.com/skynet/archive/2010/12/12/1903949.html)


## 基础

**accept**
```
int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
```
  - accept的第一个参数为服务器的socket描述字，是服务器开始调用socket()函数生成的，称为`监听socket描述字`；而accept`函数返回`的是`已连接的socket描述字`
  - 一个服务器通常通常仅仅`只创建一个监听socket描述字`，它在该服务器的生命周期内一直存在
  - 内核为`每个`由服务器进程接受的客户连接创建了一个`已连接socket描述字`，当服务器完成了对某个客户的服务，相应的已连接socket描述字就被`关闭`

**read/write**
```
#include <unistd.h>
ssize_t read(int fd, void *buf, size_t count);
ssize_t write(int fd, const void *buf, size_t count);

#include <sys/types.h>
#include <sys/socket.h>
ssize_t send(int sockfd, const void *buf, size_t len, int flags);
ssize_t recv(int sockfd, void *buf, size_t len, int flags);

ssize_t sendto(int sockfd, const void *buf, size_t len, int flags, const struct sockaddr *dest_addr, socklen_t addrlen);
ssize_t recvfrom(int sockfd, void *buf, size_t len, int flags, struct sockaddr *src_addr, socklen_t *addrlen);

ssize_t sendmsg(int sockfd, const struct msghdr *msg, int flags);
ssize_t recvmsg(int sockfd, struct msghdr *msg, int flags);
```
- read函数是负责从fd中读取内容.当读成功时，read返回实际所读的字节数，如果返回的值是0表示已经读到文件的结束了，小于0表示出现了错误。如果错误为EINTR说明读是由中断引起的，如果是ECONNREST表示网络连接出了问题。
- write函数将buf中的nbytes字节内容写入文件描述符fd.成功时返回写的字节数。失败时返回-1，并设置errno变量。 
  - 在网络程序中，当我们向套接字文件描述符写时有俩种可能:
1)write的返回值大于0，表示写了部分或者是全部的数据
2)返回的值小于0，此时出现了错误。我们要根据错误类型来处理。如果错误为EINTR表示在写的时候出现了中断错误。如果为EPIPE表示网络连接出现了问题(对方已经关闭了连接)
