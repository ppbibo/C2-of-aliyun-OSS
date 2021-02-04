基于阿里云 OSS 通信的 C&C（Demo）

在一次项目中客户主机存在安全策略，允许访问部分大厂域名，所以写了个利用阿里云 OSS 来做为中转的 DEMO，这里只是实现了命令执行，建议使用Go来编写客户端，服务端可根据个人熟悉的程序语言编写，而且该程序对于杀毒软件非常不友好，只要内置代码不要添加危险动作，简单的文件管理，命令执行基本不查杀。

---- 

## 使用方法

1.上传 execute_result.txt  oss_command_file.txt 两个文件到阿里云OSS根目录。

![57350-gkcja2r205u.png](http://www.secbook.info/usr/uploads/2020/11/3199669456.png)

2.替换两个 Python 文件代码中的 ossurl、BucketName、AccessKeyId、AccessKeySecret 参数内容。
3.被控机器运行 client.py ，攻击机运行 server.py 来执行远程命令上传到 OSS并下发到被控机器。

![123.gif](http://www.secbook.info/usr/uploads/2021/02/434934219.gif)

Tips: 编译请使用python3的pyinstaller , python2 的pyinstaller 在编译 oss2 模块时存在报错。

---- 

项目地址：https://github.com/ppbibo/C2-of-aliyun-OSS
