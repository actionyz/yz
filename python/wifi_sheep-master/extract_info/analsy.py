#!/usr/bin/python
#coding:utf-8
import socket
import dpkt
import sys
import os
import time
VICTIM_TYPE_MOBILE=0
VICTIM_TYPE_PC=1
VICTIM_TYPE_OTHER=2
class victim():
	__mac=''
	__type=VICTIM_TYPE_PC
	__behavior=[]
	__value_data=[]
	def __init__(self,mac):
		__mac=mac
	def print_mac(self):
		print 'victim_mac: %x:%x:%x:%x:%x:%x'%(ord(self.__mac[0]),ord(self.__mac[1]),ord(self.__mac[2]),ord(self.__mac[3]) , ord(self.__mac[4]),ord(self.__mac[5]) )
	def get_mobile_type(self,check_buf):
		if check_buf.find('Mi')!=-1:
			print 'find xiaomi!!!'
		self.__type='xiaomi'