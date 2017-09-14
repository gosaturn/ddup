> [socket详细介绍](https://www.cnblogs.com/skynet/archive/2010/12/12/1903949.html)


## 基础

- accept
```
int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
```
accept的第一个参数为服务器的socket描述字，是服务器开始调用socket()函数生成的，称为`监听socket描述字`；而accept`函数返回`的是`已连接的socket描述字`。
