import os
import re

hit_list = []
os.chdir('test')
# pwd = os.listdir()
# for i in pwd:
#     if os.path.isfile(i):
#         for line in open(i):
#             if re.match('.*qytang.*', line):
#                 hit_list.append(i)
#
# print('文件中包含“qytang”关键字的文件为：')
# for file_name in hit_list:
#     print(file_name)

for root, dir, file in os.walk(os.getcwd(), topdown=False):
    for name in file:
        file_names = os.path.join(root, name)
        for line in open(file_names):
            if re.match('.*qytang.*', line):
                hit_list.append(name)
print('文件中包含“qytang”关键字的文件为:')
for file_name in hit_list:
    print(file_name)
