#!/usr/bin/env python
#coding=utf-8
import pcap
import dpkt
import os
import re
import sys
import requests
def capture():
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
				print 'src_mac: %x:%x:%x:%x:%x:%x'%(ord(eth.src[0]),ord(eth.src[1]),ord(eth.src[2]),ord(eth.src[3]) , ord(eth.src[4]),ord(eth.src[5]) )
				try:
					http = dpkt.http.Request(tcp.data) or die("cant extact")
					if  len(http.headers)>0 and 'user-agent'  in http.headers and 'host' in http.headers:
						print re.findall('\(([^&]{1,})\)',http.headers['user-agent']) 
						print http.headers['host']+http.uri
						'''	
						if 'jpg' in http.uri.lower():
							dowloadPic('http:/'+http.uri,str(i)+'.jpg')
							print "****************************************************"
						if 'png' in http.uri.lower():
							dowloadPic('http:/'+http.uri,str(i)+'.png')'''

				except dpkt.dpkt.UnpackError:
					continue
				
capture()
