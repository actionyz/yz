#!/usr/bin/python
#coding:utf-8
import socket
import dpkt
import sys
import os
import time
VICTIM_TYPE_MOBILE=0
VICTIM_TYPE_PC=1
VICTIM_TYPE_UNKOWN=2
MOBILE_NAME=['xiaomi','android','apple','meizu','samang']
class victim():
	__mac=''
	type__=VICTIM_TYPE_PC
	name__=''
	__behavior=[]
	__value_data=[]
	def __init__(self,mac):
		self.__mac=mac
	def show_victim(self):
	#打印victim的信息
		if self.type__== VICTIM_TYPE_PC:
			print 'victim_type: PC'
		if self.type__== VICTIM_TYPE_MOBILE:
			print 'victim_type: MOBILE'
		print 'victim_name: %s'%(self.name__)
		print 'victim_mac: %x:%x:%x:%x:%x:%x'%(ord(self.__mac[0]),ord(self.__mac[1]),ord(self.__mac[2]),ord(self.__mac[3]) , ord(self.__mac[4]),ord(self.__mac[5]) )
	
	def get_name(self,check_buf):
		print ('finding victim name ...............')
		if check_buf.find('Mi')!=-1:
			self.name__=MOBILE_NAME[0]
		elif check_buf.find('apple') != -1:
			self.name__=MOBILE_NAME[1]
		elif check_buf.find('meizu')!= -1:
			self.name__=MOBILE_NAME[2]
		elif check_buf.find(MOBILE_NAME[3])!= -1:
			self.name__=MOBILE_NAME[3]
	def get_victim_type(self,check_buf):
		print ('finding victim type .............')
		if check_buf.find('Android')!=-1:
			self.type__=VICTIM_TYPE_MOBILE
		elif check_buf.find('windows')!=-1 or check_buf.find('linux')!=-1:
			self.type__=VICTIM_TYPE_PC