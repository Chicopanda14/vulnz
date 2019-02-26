#!/bin/python2
# -*- coding: utf-8 -*-
import os, sys, time, subprocess
from requests import get
from core.vulnzcore import *
from core.colors import *
os.system("clear")

def banner():
 print """%s
 ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗
██║   ██║██║   ██║██║     ████╗  ██║╚══███╔╝
██║   ██║██║   ██║██║     ██╔██╗ ██║  ███╔╝ 
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║ ███╔╝  
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████╗ 
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ %sv.1.5                                           
%s"""%(yellow, white, end)

def help():
 os.system("clear")
 banner()
 print """
 Commands:                                             
 whois[0] :  get information about a website           
 port scanning[1]  : port scan, get  portsclosed and  open
 GeoIP[2]          : get ip info
 TraceRoute[3]     : traceroute
 Dns Lookup[4]     : Get dns lookup 
 exit[99]          : Exit
 """                                                  
 menu()

def menu():
 print '''
 %s0.%swhois
 %s1.%sport scan
 %s2.%sGeo Ip
 %s3.%sTraceRoute
 %s4.%sDns Lookup
 %s5.%sSubnet Lookup
 %s09.%sHelp
 %s99.%sExit
 %s'''%(red, green, red, green, red,
green, red, green, red, green, red,
green, red,
green, red, green, end)

def main():
 while True: 
   select = raw_input("%s>>%s "%(red, end))
   if select == "0":
    whois()
   elif select == "1":
    port_scan()
   elif select == "2":
    country_lookup()
    print ""
   elif select == "3":
    traceroute()
   elif select == "4":
    dns_lookup()
   elif select == "5":
    sub_lookup()
   elif select == "09":
    help()
   elif select == "99" or select == "exit":
    print "[!] Exiting."
    time.sleep(2)
    sys.exit()
   else:
    print "[!] wrong command!"
    time. sleep(2)
    program_restart()

def control():
    try:
        banner()
        menu()
        main()
    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detected, Exiting. . .")
        time.sleep(2)
        sys.exit()
        
if __name__ == "__main__":
 control()
