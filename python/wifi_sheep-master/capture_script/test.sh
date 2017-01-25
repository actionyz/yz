#!/bin/sh
time=0
while [ "$time" -lt 10 ]
do
	time=$(($time+1))	
	filename="dns_$time.pcap"
	echo tcpdump -i wlan1 port 53  -c 30 >>  "../pcap/$filename"
	tcpdump -i wlan1 port 53 -c 30 >> "../pcap/$filename"
done

