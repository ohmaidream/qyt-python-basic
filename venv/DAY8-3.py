import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return True
    else:
        return False

if __name__ == '__main__':
    result = qytang_ping('192.168.1.254')
    if result == True:
        print("request is reachable")
    elif result == False:
        print("no response")

