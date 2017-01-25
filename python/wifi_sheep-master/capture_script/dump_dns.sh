#!/bin/sh
sudo tcpdump -i wlan1 port 53  -c 30 >> pcap/dns.log
