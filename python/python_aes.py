# python aes 加解密
'''
参数介绍:
  key:16\24\32位的密钥
  model:加解密的方式,有MODE_ECB MODE_CBC MODE_CFB
  iv:ecb和ctr模式不需要,是一个初始化加解密向量,默认是一堆block_size大小的0 且为binary型(block_size可以使用AES.block_size查看)
  text必须为16的整数倍,不足补0
加密算法:
  ECB
    简单；
    有利于并行计算；
    误差不会被传送；
    不能隐藏明文的模式；
    可能对明文进行主动攻击；
  CBC
    不容易主动攻击,安全性好于ECB,适合传输长度长的报文,是SSL、IPSec的标准。
    不利于并行计算；
    误差传递；
    需要初始化向量IV;
  CFB
    隐藏了明文模式;
    分组密码转化为流模式;
    可以及时加密传送小于分组的数据;
    不利于并行计算;
    误差传送：一个明文单元损坏影响多个单元;
    唯一的IV;

'''

from Crypto.Cipher import AES
cryptor = AES.new(key, AES.MODE_CFB, iv)
cryptor.encrypt(text)
