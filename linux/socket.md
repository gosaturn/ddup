> [socket详细介绍](https://www.cnblogs.com/skynet/archive/2010/12/12/1903949.html)


## 基础

- accept
```
int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
```
  - accept的第一个参数为服务器的socket描述字，是服务器开始调用socket()函数生成的，称为`监听socket描述字`；而accept`函数返回`的是`已连接的socket描述字`
  - 一个服务器通常通常仅仅`只创建一个监听socket描述字`，它在该服务器的生命周期内一直存在
  - 内核为`每个`由服务器进程接受的客户连接创建了一个`已连接socket描述字`，当服务器完成了对某个客户的服务，相应的已连接socket描述字就被`关闭`
