#!/usr/bin/env python3
#! -*- coding=utf-8 -*-

# from ping2 import qytang_ping
from ssh import qytang_ssh
import re
import pprint

def qytang_get_if(*ips, username='iseadmin', password='Ise1611'):
    device_if_dict = {}
    for ip in ips:
    #     if qytang_ping(ip):
    #         print(f'ping {ip} is successful, trying ssh...')
        qytang_ssh(ip, username, password, cmd='sh ip int bri')
        for line in open(ip):
            match = re.match('(\w+\d/?\d?)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.*', line)
            if match:
                l1 = list(match.groups()[0])
                print(l1)


if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.152.2'), indent=4)

