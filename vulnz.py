#!/bin/python2
import os, sys, time, subprocess
from requests import get
from core.vulnzcore import *
os.system("clear")

def banner():
 print """\033[0m
   **      **          **
 /**     /**         /**
/**     /** **   ** /** *******  ******
//**    ** /**  /** /**//**///**////**
  //**  **  /**  /** /** /**  /**   **
   //****   /**  /** /** /**  /**  **
     //**    //****** *** ***  /** ******
     //      ////// /// ///   // //////

 \t         [*] Made by: Mr.Z3r0 [*]
 \t           [*] Testing Tool [*]
 \t  [*] I love you, thanks for using. [*]
 \t           [*] version 1.0. [*]
"""

def help():
 os.system("clear")
 banner()
 print """
 Commands:                                             
 whois[0] :  get information about a website           
 port scanning[1]: port scan, get  ports
 closed and  open
 GeoIP[2]: get ip info
 exit[9]:  exit framework
 """                                                  
 menu()

def menu():
 print "\033[1;31;40mOptions:"
 print '''\033[1;32;40m
 [0]whois
 [1]port scanning
 [2]GeoIP
 [3]TraceRoute
 [4]Dns Lookup
 [5]help
 [6]commands
 [7]banner
 [9]exit
 '''
def main():
 while True: 
   select = raw_input("\033[1;31;40m>>\033[0m  ")
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
    help()
   elif select == "6":
    menu()
   elif select == "7":
    banner()
   elif select == "9":
    print "[!] Exting."
    time.sleep(2)
    os.system("clear") 
    sys.exit()
   else:
    print "[!] wrong command!"
    time. sleep(5)
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
