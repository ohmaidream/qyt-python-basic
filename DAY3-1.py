import re
str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/1'
tuples = re.match('(\d+)\s(\w{4}\.\w{4}\.\w{4})\s(\w+)\s(.*)', str1).groups()

print("VLAN ID    : %s" % tuples[0])
print("MAC        : %s" % tuples[1])
print("Type       : %s" % tuples[2])
print("Interface  : %s" % tuples[3])
