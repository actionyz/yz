#! /bin/bash
case $1 in
    "start")
       sleep 1
       ifconfig wlan1 down
       sleep 1
       iwconfig wlan1 mode monitor
       sleep 1
       ifconfig wlan1 up
       sleep 2
       airmon-ng start wlan1
       sleep 1
       airbase-ng -e hellotest  -c 11 wlan1
       sleep 1
    ;;
    "atup")
       sleep 1
       ifconfig at0 up
       sleep 1
       ifconfig at0 12.0.0.1 netmask 255.255.255.0
       sleep 1
       route add -net 12.0.0.0 netmask 255.255.255.0 gw 12.0.0.1
       sleep 1
       echo “1” &gt;/proc/sys/net/ipv4/ip_forward
       sleep 2
       dhcpd -cf /etc/dhcp/dhcpd.conf -pf /var/run/dhcpd.pid at0
       sleep 2
       service isc-dhcp-server start
       sleep 1
    ;;
    "startnat")
       sleep 1
       iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
       sleep 1
       iptables -A FORWARD -i wlan1 -o wlan0 -j ACCEPT
       sleep 1
       iptables -A FORWARD -p tcp –-syn -s 12.0.0.0/24 -j TCPMSS –set-mss 1356
       sleep 2
    ;;*)
       echo “Usage $0 {start|atup|startnat}”
    ;;
    esac
