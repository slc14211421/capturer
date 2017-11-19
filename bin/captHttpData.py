#_*_encoding:utf-8_*_
'''
Created on November 16, 2017

@author: LisonSong
'''

import pcap
import dpkt
import logging
import logging.config
import  commonTools
from multiprocessing import Process, Pool

#config logging
logging.config.fileConfig("../conf/logger.conf")
logger = logging.getLogger("captHttpData")

#loading config
confdit=commonTools.lodConfig()

#time sip dip sport dport method requestUri user-agent
outformat="\"%s\"\t\"%s\"\t\"%s\"\t\"%s\"\t\"%s\"\t\"%s\"\t\"%s\"\t\"%s\""



def captData():
    pc=pcap.pcap(confdit['Ethernet'])
    pc.setfilter('tcp')
    process = Pool(int(confdit['CoreNumber']))
    for ptime,pdata in pc:
        #anlyCap(ptime,pdata)
        #mythread=commonTools.ThreadFunc(anlyCap,(ptime,pdata),anlyCap.__name__)
        #mythread.start()
        process.apply_async(anlyCap,args=(ptime,pdata))


def anlyCap(ptime,pdata):
    p=dpkt.ethernet.Ethernet(pdata)
    ip_data=p.data
    tcp_data=ip_data.data
    if (tcp_data.data.decode('utf-8').find("GET")==0) or \
       (tcp_data.data.decode('utf-8').find("POST")==0):
        srcip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.src)))
        dstip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.dst)))
        sport = tcp_data.sport
        dport = tcp_data.dport
        try:
            h_data=dpkt.http.Request(tcp_data.data)
            userAgent=h_data.headers['user-agent']
            requestUri="http://"+h_data.headers['host']+h_data.uri
            method=h_data.method
            logger.info(outformat % (str(commonTools.formattime(ptime)), srcip, dstip, str(sport), str(dport), method, requestUri,userAgent))
        except:
            pass

if __name__=='__main__':
    captData()




