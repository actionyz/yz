#!/usr/bin/env python
#coding=utf-8
import dpkt
f = open('dns.pcap')
pcap = dpkt.pcap.Reader(f)
i = 0
icmp6 = dpkt.icmp6.ICMP6()
icmp = dpkt.icmp.ICMP()
#print type(icmp)
for ts,buf in pcap:
	i = i+1
	eth = dpkt.ethernet.Ethernet(buf)
	ip = eth.data
	tcp = ip.data
	print i
	#print type(tcp)
	#if type(tcp) != type('asd'):
	if type(tcp) != type(icmp) and type(tcp)!=type(icmp6) and len(tcp) > 0 and tcp.dport != 80:
		#print tcp.__class__.__name__
		#print str(tcp.data)
		if(len(tcp.data)>0):
			http = dpkt.http.Response(tcp.data) 
			'''
			print len(http.headers)
			print 'src_mac: %x:%x:%x:%x:%x:%x'%(ord(eth.src[0]),ord(eth.src[1]),ord(eth.src[2]),ord(eth.src[3]) , ord(eth.src[4]),ord(eth.src[5]) )
			print http.headers
			print http.headers['host']+http.uri
			'''
f.close()