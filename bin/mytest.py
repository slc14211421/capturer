#_*_encoding:utf-8_*_

import pcap
import dpkt
import time

#time sip dip sport dport requestUri user-agent
outformat="\"%s\"\t\"%s\"\t\"%s\"\t\"%s\"\t\"%s\"\t\"%s\"\t\"%s\""

def formattime(t):  # 日期字段格式化
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t + 8 * 3600))

def captData():
    pc=pcap.pcap('eth0')
    pc.setfilter('tcp')
    for ptime,pdata in pc:
        anlyCap(ptime,pdata)

def anlyCap(ptime,pdata):
    p=dpkt.ethernet.Ethernet(pdata)
    ip_data=p.data
    tcp_data=ip_data.data
    #print tcp_data
    if p.data.__class__.__name__=='IP':
        if tcp_data.__class__.__name__=='TCP':
            srcip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.src)))
            dstip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.dst)))
            sport = tcp_data.sport
            dport = tcp_data.dport

            try:
                h_data=dpkt.http.Request(tcp_data.data)
                userAgent=h_data.headers['user-agent']
                requestUri="http://"+h_data.headers['host']+h_data.uri
                print outformat % (str(formattime(ptime)), srcip, dstip, str(sport), str(dport),requestUri,userAgent)
            except Exception,e:
                pass
                #print " NOT HTTP"
                #print e.message



if __name__=='__main__':
    captData()




