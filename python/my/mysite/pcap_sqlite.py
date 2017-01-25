#!/usr/bin/env python
#coding=utf-8
import pcap
import dpkt
import os
import re
import requests
import sqlite3
conn = sqlite3.connect("db.sqlite3")  
def dowloadPic(imageUrl,filePath):
    r = requests.get(imageUrl) or die("error")
    with open(filePath, "wb") as code:
        code.write(r.content)

fp = open(r'c:\url.txt','ab')
pc = pcap.pcap()
b = 'tcp port 80'
pc.setfilter(b)
i = 0
icmp6 = dpkt.icmp6.ICMP6()
icmp = dpkt.icmp.ICMP()
for ts,buf in pc:
	
	eth = dpkt.ethernet.Ethernet(buf)
	ip = eth.data
	tcp = ip.data
	
	#print type(tcp)
	#if type(tcp) != type('asd'):
	if type(tcp) != type(icmp) and type(tcp)!=type(icmp6) and len(tcp) > 0 and tcp.dport == 80:
		#print tcp.__class__.__name__
		#print str(tcp.data)
		if(len(tcp.data)>0):
			i = i+1
			print i
			mac = 'src_mac: %x:%x:%x:%x:%x:%x'%(ord(eth.src[0]),ord(eth.src[1]),ord(eth.src[2]),ord(eth.src[3]) , ord(eth.src[4]),ord(eth.src[5]) )
			print mac
			try:
				http = dpkt.http.Request(tcp.data) or die("cant extact")
				if  len(http.headers)>0 and 'user-agent'  in http.headers and 'host' in http.headers:
					useragent = re.findall('\(([^&]{1,})\)',http.headers['user-agent']) 
					if len(useragent) > 0:
						print useragent[0]
						print http.headers['host']+http.uri
						sql = "insert into victim(id,useragent,mac)values('"+str(i)+"','"+useragent[0]+"','"+mac+"')"  
						conn.execute(sql)
						conn.commit()
					'''	
					if 'jpg' in http.uri.lower():
						dowloadPic('http:/'+http.uri,str(i)+'.jpg')
						print "****************************************************"
					if 'png' in http.uri.lower():
						dowloadPic('http:/'+http.uri,str(i)+'.png')'''

			except dpkt.dpkt.UnpackError:
				continue

'''			
for ts,pkt in pc:
#    print `dpkt.ethernet.Ethernet(pkt)`
    Eth = dpkt.ethernet.Ethernet(pkt)
    length = Eth.data.len
    tcp = Eth.data.data
#    print type(length)
    if length > 48 and tcp.data:
    	
        content = str(tcp.data)
        #http = dpkt.http.Request(tcp.data)
        #print http.uri
        if 'GET' in content:
            url = content.split()[1]
            print url
            fp.write(url+'\r\n')
            fp.flush()
#        print '--------------------------------------------------'
#        print str(`Eth.data.data.data`)
#        print str(`Eth.data.data.data`).split()[1]
#        print '--------------------------------------------------'
fp.close()
'''