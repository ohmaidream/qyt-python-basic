import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n" \
           "TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}
for conn in asa_conn.split('\n'):
    src_ip = re.match('TCP Student (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) Teacher '
                  '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes (\d+), flags ([A-Za-z]+)', conn).groups()[0]
    dst_ip = re.match('TCP Student (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) Teacher '
                  '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes (\d+), flags ([A-Za-z]+)', conn).groups()[2]
    src_port = re.match('TCP Student (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) Teacher '
                  '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes (\d+), flags ([A-Za-z]+)', conn).groups()[1]
    dst_port = re.match('TCP Student (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) Teacher '
                  '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes (\d+), flags ([A-Za-z]+)', conn).groups()[3]
    byte = re.match('TCP Student (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) Teacher '
                  '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes (\d+), flags ([A-Za-z]+)', conn).groups()[4]
    flag = re.match('TCP Student (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}) Teacher '
                  '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).*bytes (\d+), flags ([A-Za-z]+)', conn).groups()[5]
    tuple_1 = (src_ip, src_port, dst_ip, dst_port)
    tuple_2 = (byte, flag)
    asa_dict[tuple_1] = tuple_2
print("打印分析后的字典：\n")
print(asa_dict)
print("格式化打印输出\n")
for key, value in asa_dict.items():
    print('{0:^10}:{1:^15}|{2:^10}:{3:^15}|{4:^10}:{5:^15}|{6:^10}:{7:^15}'.format('src', key[0], 'src_port', key[1],
                                                                                   'dst', key[2], 'dst_port', key[3]))
    print('{0:^10}:{1:^15}|{2:^10}:{3:^15}'.format('bytes', value[0], 'flags', value[1]))
    print('=' * 110)
