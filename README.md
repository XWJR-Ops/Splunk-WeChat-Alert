# Splunk-WeChat-Alert  
splunk微信告警脚本   
### 功能介绍  
1. 用于将splunk告警信息推送到微信企业号
2. 企业微信有3种方式：用户名发送、部门发送、标签发送（将相关用户加入一个标签）
3. 本脚本采用标签的形式发送，具体见 [企业微信开发文档](https://work.weixin.qq.com/api/doc#10167/文本消息)
4. splunk触发报警脚本时，会传8个变量，取第8个变量（报警信息gzip压缩包的路径），解压gzip，读取csv，取出日志信息
5. 开发环境**python2**

### 安装使用  
#### 环境要求  
1. 需要注册微信企业号  
[点击注册](https://qy.weixin.qq.com/)

#### 使用  

1. 安装所需模块
```shell
pip install requests
```
2. 下载
```shell
git clone https://github.com/XWJR-Ops/Splunk-WeChat-Alert.git
```
3. 复制脚本到执行位置
```shell
cd Splunk-WeChat-Alert
cp splunk.py /opt/splunk/bin/scripts
chown splunk.splunk /opt/splunk/bin/scripts/splunk.py
chmod 755 /opt/splunk/bin/scripts/splunk.py
```
4. splunk创建告警
splunk创建告警时，触发操作选择运行脚本，脚本名称**splunk.py**



