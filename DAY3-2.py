import re
str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
tuples = re.match('(.*)\sserver\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\slocalserver\s\
(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+),\sidle\s(\d+):(\d+):(\d+),\sbytes\s(\d+),\sflags\s(.*)', str1).groups()

print("protocol          : %s" % tuples[0])
print("server            : %s" % tuples[1])
print("localserver       : %s" % tuples[2])
print("idle              : %s小时 %s分钟 %s秒" % (tuples[3], tuples[4], tuples[5]))
print("bytes             : %s" % tuples[6])
print("flags             : %s" % tuples[7])
