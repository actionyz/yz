import time
import thread
import pcap
import dpkt
import os
import re
import requests
from django.shortcuts import render
from django.http import HttpResponse
from yz import models
# Create your views here.

user_list = [
	{"user":"jack","pwd":"abc"},
	{"user":"tom","pwd":"ABC"},
]

def index(request):
	#print "<b>OK</b>"
	#return HttpResponse("helloword")
	'''
	try:
		thread.start_new_thread(capture,())
	except:
		print "Error: unable to start thread"
	'''
	if request.method == "POST":
		username = request.POST.get("username",None)
		password = request.POST.get("password",None)
		#print (username,password)
		temp = {"user":username,"pwd":password}
		user_list.append(temp)
	return render(request,"index.html",{"data":user_list})
def test(request):
	#print "<b>OK</b>"
	#return HttpResponse("helloword")
	if request.method == "POST":
		username = request.POST.get("username",None)
		password = request.POST.get("password",None)
		#print (username,password)
		models.person.objects.create(user = username,pwd = password)
		user_list = models.person.objects.all()
	return render(request,"test.html",{"data":user_list})
