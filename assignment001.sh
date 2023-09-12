#!bin/bash
#write a bash/shell script to get the tcpdump of a process on your PC or entire system

ifconfig | less  #shows all available network interfaces

sudo tcpdump -i wlo1 -n #capturing network packets from  wlo1 interface
