#!/usr/bin/python
#coding:utf-8
import socket
import dpkt
import copy
import sys
import os
import re
import time
import analyse
from pwn import re, sys

TCP_PORT_HTTP=80
GLB_macs={} #全局的mac地址和victims对应的表
GLB_victims_num = 0
GLB_victims=[]
UDP_PROTO_DNS=53
def mac2victim(mac):
    return GLB_macs[mac]
def extrace_data(pcap_name):
    global GLB_macs,GLB_victims_num,GLB_victims
    pcapReader = dpkt.pcap.Reader(file(pcap_name, "rb"))
    seq=1
    '''
    局部变量
    cur_victim 当前的victim
    cur_mac 当前的mac
    '''
    for ts, data in pcapReader: #ts是数据包的时间戳 #data是数据包的内容
        eth = dpkt.ethernet.Ethernet(data) #以太网的数据头
        print '包序号:%d'%seq
        seq+=1
        print 'src_mac: %x:%x:%x:%x:%x:%x'%(ord(eth.src[0]),ord(eth.src[1]),ord(eth.src[2]),ord(eth.src[3]) , ord(eth.src[4]),ord(eth.src[5]) )
        print 'dst_mac: %x:%x:%x:%x:%x:%x'%(ord(eth.dst[0]),ord(eth.dst[1]),ord(eth.dst[2]),ord(eth.dst[3]) , ord(eth.dst[4]),ord(eth.dst[5]) )
        print '以太网承载协议: %d'%(eth.type)
        if not GLB_macs.has_key(eth.src): #如果这个mac地址不在字典里面
            n_victim= analyse.victim(eth.src)
            GLB_victims_num +=1
            GLB_macs[eth.src]=n_victim #把当前的mac加入到字典中去
        cur_mac=eth.src
        if eth.type==dpkt.ethernet.ETH_TYPE_IP: #如果是IP包
            if isinstance(eth.data, dpkt.ip.IP):
                if isinstance(eth.data.data, dpkt.tcp.TCP): #如果是TCP包
                    dport=eth.data.data.dport
                    sport=eth.data.data.sport
                    print 'src-port: %d dst-port: %d'%(sport,dport)
                    if dport==TCP_PORT_HTTP:  #请求包，目的端口是80
                        if len(eth.data.data.data) >0:   #80端口对应的数据长度大于0,即是http包
                            if eth.data.data.seq!=0: #是分片包，此处应该另做处理
                                print eth.data.data.seq
                                pass    
                            else:
                                print eth.data.data.seq
                                raw_input()
                                #print eth.data.data.data
                                http_request=dpkt.http.Request(eth.data.data.data)
                                print http_request.headers     #请求头
                                #print GLB_macs[eth.src].__mac
                                if GLB_macs[eth.src].type__==analyse.VICTIM_TYPE_UNKOWN:
                                    GLB_macs[eth.src].get_victim_type(eth.data.data.data)
                                elif GLB_macs[eth.src].name__=='':
                                    GLB_macs[eth.src].get_name(eth.data.data.data)
                                #raw_input()
                    if sport==TCP_PORT_HTTP:   #响应包
                        if len(eth.data.data.data)>0:
                            if eth.data.data.seq !=0: #是分片包，此处应该另做处理
                                pass
                            else:
                                print eth.data.data.data
                                http_response= dpkt.http.Response(eth.data.data.data)
                                #print 'response'
                                print http_response.headers
                if eth.data.p==dpkt.ip.IP_PROTO_UDP: #udp协议的包
                    print eth.data.data
                    if isinstance(eth.data.data,dpkt.udp.UDP):
                        if eth.data.data.dport==UDP_PROTO_DNS: #DNS协议
                            dns_pcap=dpkt.dns.DNS(eth.data.data.data)
                            dns_qurey="%s"%(dns_pcap.qd)
                            re_find_dns= re.compile(r"'([^']*)'")
                            dns_qurey=re_find_dns.findall(dns_qurey)
                            cur_victim=mac2victim(cur_mac)
                            for i in dns_qurey:
                                pass#cur_victim.behavior__.append(i)
                            #udp请求包
    print 'whole pcap has %d victims'%(GLB_victims_num)
    for (d,x) in GLB_macs.items():
        x.show_victim()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        extrace_data(file_name)
    else:
        print "argvs:pcap_name"

    '''if len(sys.argv) == 2:
                    file_list = os.listdir(sys.argv[1])
                    for pcap in file_list:
                        pcap_addr = sys.argv[1]  + pcap
                        get_flags_num(pcap_addr)
                else:
                    print "argvs:input_folder"
            '''