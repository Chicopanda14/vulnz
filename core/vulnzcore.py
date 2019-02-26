import sys, os, time
from requests import get
from re import findall
from tld import get_tld
from requests import get
def program_restart():
   python = sys.executable
   os.execl(sys.executable, sys.executable, *sys.argv)
   curdir = os.getcwd()

def banner():
 print """\033[1;32;40m
   **      **          **
 /**     /**         /**
 /**     /** **   ** /** *******  ******
 //**    ** /**  /** /**//**///**////**
  //**  **  /**  /** /** /**  /**   **
   //****   /**  /** /** /**  /**  **
     //**    //****** *** ***  /** ******
     //      ////// /// ///   // //////

 \t [*] Made by: Mr.Z3ro
 \t [*] Testing Tool
 """



def whois():
 inp = raw_input("domain or ip >> ")
 result = get('http://api.hackertarget.com/whois/?q=' + inp).text
 sys.stdout.write(result)
def port_scan():
 inp = raw_input("Ip or domain >> ")
 result = get('http://api.hackertarget.com/nmap/?q=' +inp).text
 sys.stdout.write(result)
def country_lookup():
  ip = raw_input("ip >> ")
  result = get("http://api.hackertarget.com/geoip?q=" +ip).text
  sys.stdout.write(result)
def traceroute():
  ip = raw_input("Ip >> ")
  result  = get("https://api.hackertarget.com/mtr/?q=" +ip).text
  sys.stdout.write(result)
def  dns_lookup():
 ip = raw_input("Ip or domain >> ")
 result = get("http://api.hackertarget.com/dnslookup/?q=" +ip).text
 sys.stdout.write(result)
def sub_lookup():
 ip = raw_input("Ip or domain>> ")
 result = get("http://api.hackertarget.com/subnetcalc/?q=" +ip).text
 sys.stdout.write(result + "\n")
