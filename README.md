# capturer
pypcap  dpkt  完成报文抓取和http 解析

目前只做到了功能性开发、 高并发处理能力很差、需要找解决方案。

## Install 

1、
yum install libcap libcap-devel

或者从os 镜像中拷贝出对应的 rpm 包安装

2、

将程序包放到opt 上解压 

cd /opt/capturer/envInstall; sh install.sh

## Config

/opt/capturer/conf/capturer.conf    配置抓包网卡

## Run

/opt/python27/bin/python captHttpData.py &
 
