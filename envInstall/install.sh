#!/bin/bash

function printResult()
{
 if [ $2 -ne 0 ]; then
    echo -e "\033[31m ################ [ $1 install Faild ]\033[0m"
 else
    echo -e "\033[32m ################ [ $1 install Success ] \033[0m"
 fi
}
declare -A dic


cd /opt/capturer/envInstall/
tar xvf Python-2.7.9.tar.xz
cd Python-2.7.9
./configure --prefix=/opt/python27 ;make ;make install
dic["Python-2.7.9"]=$?
cd ../;rm Python-2.7.9 -rf

cd /opt/capturer/envInstall/
tar zxvf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
/opt/python27/bin/python setup.py install
dic["setuptools-0.6c11"]=$?
cd ../;rm setuptools-0.6c11 -rf


cd /opt/capturer/envInstall/
tar zxvf pip-9.0.1.tar.gz
cd pip-9.0.1
/opt/python27/bin/python setup.py install
dic["pip-9.0.1"]=$?
cd ../;rm pip-9.0.1 -rf

cd /opt/capturer/envInstall/
tar zxvf simplejson-3.5.2.tar.gz
cd simplejson-3.5.2
/opt/python27/bin/python setup.py install
dic["simplejson-3.5.2"]=$?
cd ../;rm simplejson-3.5.2 -rf

cd /opt/capturer/envInstall/
tar zxvf requests-2.13.0.tar.gz
cd requests-2.13.0
/opt/python27/bin/python setup.py install
dic["requests-2.13.0"]=$?
cd ../;rm requests-2.13.0 -rf

cd /opt/capturer/envInstall/
unzip pytz-2017.3.zip
cd pytz-2017.3
/opt/python27/bin/python setup.py install
dic["pytz-2017.3"]=$?
cd ../;rm pytz-2017.3 -rf

cd /opt/capturer/envInstall/
tar zxvf dpkt-1.9.1.tar.gz
cd dpkt-1.9.1
/opt/python27/bin/python setup.py install
dic["dpkt-1.9.1"]=$?
cd ../;rm dpkt-1.9.1 -rf


cd /opt/capturer/envInstall/
tar zxvf pypcap-1.2.0.tar.gz
cd pypcap-1.2.0
/opt/python27/bin/python setup.py install
dic["pypcap-1.2.0"]=$?
cd ../;rm pypcap-1.2.0 -rf


for key in $(echo ${!dic[*]})
do
        #echo "$key : ${dic[$key]}"
        printResult $key ${dic[$key]}
done
