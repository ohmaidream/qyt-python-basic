import re
import time
import os

while True:
    try:
        time.sleep(2)
        netstat_result = os.popen("netstat -tulnp").read()
        print("等待一秒重新开始监控！")
    except re.match('.*tcp.*(0.0.0.0:80)\s+.*', netstat_result):
        print("HTTP(TCP/80)服务已经被打开")
        break

