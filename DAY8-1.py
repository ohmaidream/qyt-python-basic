import re
import time
import os

trigger = 'null'
while True:
    time.sleep(2)
    print("等待一秒重新开始监控！")
    for netstat_result in os.popen("netstat -tulnp").read().split("\n"):
        if re.match('.*tcp.*0.0.0.0:80\s+.*', netstat_result):
            print("HTTP(TCP/80)服务已经被打开")
            trigger = 'break'
    if trigger == 'break':
        break



