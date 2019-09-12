#!/usr/bin/env python
'''
Author: Veerndra Kakumanu
Description: Simple test script
Usage: python test.py <IP> <PORT>
'''
import json
import sys
try:
    import requests
except ImportError:
    print "Install requests python module-> pip install requests"
    exit(1)

if len(sys.argv) == 3:
    try:
        IP = sys.argv[1]
        PORT = int(sys.argv[2])
    except TypeError:
        print "Usage: python test.py <IP> <PORT>"
else:
    print "Usage: python test.py <IP> <PORT>"
#IP = "192.168.39.228"
#PORT = 32438
URL = "http://{}:{}".format(IP, PORT)
HEADERS = {'Content-Type': 'application/json'}
COLOR_CODES = ["#C0C0C0", "#808080",
               "#000000", "#FF0000",
               "#800000", "#FFFF00",
               "#808000", "#00FF00",
               "#008000", "#00fFFF",
               "#008080", "#0000FF",
               "#000080", "#fF00FF",
               "#800080"]
BAD_COLOR_REQ = ["#GGGGGGG", "#12121212FF",
                 "$0000FF", "#$A0000",
                 "#AAAA7", "AAAAFF"]
GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

print GREEN+"[+] Running Positive Test Cases"+ENDC
for codes in COLOR_CODES:
    payload = json.dumps({"code": codes})
    res = requests.post(url=URL, headers=HEADERS, data=payload)
    print "[*] PAYLOAD => {}, RESPONSE=> {}, RESPOSE CODE=> ".format(payload, res.text, res.status_code )+RED+str(res.status_code)+ENDC
print GREEN+"[+] Running Negetive Test Cases"+ENDC
for codes in BAD_COLOR_REQ:
    payload = json.dumps({"code": codes})
    res = requests.post(url=URL, headers=HEADERS, data=payload)
    print "[.] PAYLOAD => {}, RESPONSE=> {}, RESPOSE CODE=> ".format(payload, res.text, res.status_code )+RED+str(res.status_code)+ENDC


