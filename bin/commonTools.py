#_*_encoding:utf-8_*_
'''
Created on November 16, 2017

@author: LisonSong
'''
import ConfigParser
import time
import os

def formattime(t):  # 日期字段格式化
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t + 8 * 3600))

def lodConfig():
    basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print basedir
    confdit={}
    conf=ConfigParser.ConfigParser()
    conf.read(basedir+"/conf/capturer.conf")
    confdit['Ethernet']=conf.get('captHttpData','Ethernet')
    return confdit
