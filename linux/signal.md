## 信号
> [信号处理机制](http://www.cnblogs.com/taobataoma/archive/2007/08/30/875743.html)

`信号`是用来通知进程发生了某个`异步事件`
进程在`从内核态返回用户态时`处理信号
可以通过signal系统调用，指定信号的处理函数
