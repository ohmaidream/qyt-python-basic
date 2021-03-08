import re
str1 = 'Port-channel1.189    192.168.189.254 YES  CONFIG up     up'

tuples = re.match('(^Port.*\d)\s+(\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3}).*(up|down)', str1).groups()

print('-' * 80)
print("接口     ： %s" % tuples[0])
print("IP地址   ： %s" % tuples[1])
print("状态     ： %s" % tuples[2])
