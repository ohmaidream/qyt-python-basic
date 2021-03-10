import re
# ip_addr = input("IP=")
# mask = input("mask=")
ip_addr = '192.168.20.20'
mask = '255.255.255.252'

if int(re.match('\d{1,3}\.(\d{1,3})\.\d{1,3}\.\d{1,3}', mask).groups()[0]) != 255 or \
   int(re.match('(\d{1,3})\.\d{1,3}\.\d{1,3}\.\d{1,3}', mask).groups()[0]) != 255:
    print("Sorry, mask shorter than /16 is not available now.")
elif int(re.match('255\.255\.(\d{1,3})\.\d{1,3}', mask).groups()[0]) != 255:
    ipaddr_3 = int(re.match('\d{1,3}\.\d{1,3}\.(\d{1,3})\.\d{1,3}', ip_addr).groups()[0])
    mask_3 = int(re.match('\d{1,3}\.\d{1,3}\.(\d{1,3})\.\d{1,3}', mask).groups()[0])
    gw_3 = (256 - mask_3) * (ipaddr_3 // (256 - mask_3) + 1) - 1
    net_3 = (256 - mask_3) * (ipaddr_3 // (256 - mask_3))
    ipv4_gw = re.match('(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}', ip_addr).groups()[0] + "." + \
              re.match('(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}', ip_addr).groups()[1] + "." + \
              str(gw_3) + ".254"
    net = re.match('(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}', ip_addr).groups()[0] + "." + \
          re.match('(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}', ip_addr).groups()[1] + "." + \
          str(net_3) + ".0"
    print('GW=%s' % ipv4_gw)
    print('Network=%s' % net)
elif int(re.match('255\.255\.(\d{1,3})\.\d{1,3}', mask).groups()[0]) == 255:
    if int(re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})', mask).groups()[0]) < 252:
        ipaddr_4 = int(re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})', ip_addr).groups()[0])
        mask_4 = int(re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.(\d{1,3})', mask).groups()[0])
        gw_4 = (256 - mask_4) * (ipaddr_4 // (256 - mask_4) + 1) - 1
        net_4 = (256 - mask_4) * (ipaddr_4 // (256 - mask_4))
        ipv4_gw = re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.\d{1,3}', ip_addr).groups()[0] + "." + \
                  re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.\d{1,3}', ip_addr).groups()[1] + "." + \
                  re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.\d{1,3}', ip_addr).groups()[2] + "." + str(gw_4)
        net = re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.\d{1,3}', ip_addr).groups()[0] + "." + \
              re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.\d{1,3}', ip_addr).groups()[1] + "." + \
              re.match('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.\d{1,3}', ip_addr).groups()[2] + "." + str(net_4)
        print('GW=%s' % ipv4_gw)
        print('Network=%s' % net)
    else:
        print("Sorry, this is a point-to-point network OR mask input error")


