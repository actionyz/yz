##wifi_sheep
>旨在完成一个类似blackhat大会上的绵羊墙，主要思路是在受害者在通过我们的AP上网的前提下，通过抓取流量，并对流量进行分析提取，并展现出来。Ps这么一讲似乎没啥好做的～～～～（＞＿＜）～～～～
capture_script文件夹下放的抓包的脚本
extract_info文件夹下放的是提取信息的脚本
pcap文件夹用来存放抓到的包

###怎么抓包？
抓包思路是不用wireshark抓，用tcpdump抓，这样可以少掉很多不必的信息，但是tcp的包似乎还是得抓成pcap包的模式，这个到时候再说。

###环境搭建
建议环境:Ubuntu14.04 + 腾达311u+(RT3070芯片linux下免驱)+ hostapd + dnsmaq
搭建链接：http://my.oschina.net/oldfeel/blog/292264 
另一个dns开启不了的bug修复https://bugs.launchpad.net/ubuntu/+source/wpa/+bug/1289047 

hostapd.conf设置样板

```bash
interface=wlan1
driver=nl80211
ssid=ubuntu-ap 
hw_mode=g
channel=11
dtim_period=1
rts_threshold=2347
fragm_threshold=2346
macaddr_acl=0
auth_algs=3
ieee80211n=0
#wpa=3
#wpa_passphrase=12345678
#wpa_key_mgmt=WPA-PSK
#wpa_pairwise=TKIP
rsn_pairwise=CCMP
```
