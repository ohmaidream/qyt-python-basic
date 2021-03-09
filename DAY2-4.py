department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

# line1 = "Department1 name:%-11sManager:%-11sCOURSE FEES:%-11.2fThe End!" \
#         % (department1, depart1_m, COURSE_FEES_SEC)
# line2 = "Department1 name:%-11sManager:%-11sCOURSE FEES:%-11.2fThe End!" \
#         % (department2, depart2_m, COURSE_FEES_Python)

line1 = 'Department1 name:{0:<11}Manager:{1:<11}COURSE FEES:{2:<11.2f}The End!'.format(department1, depart1_m, COURSE_FEES_SEC)
line2 = 'Department1 name:{0:<11}Manager:{1:<11}COURSE FEES:{2:<11.2f}The End!'.format(department2, depart2_m, COURSE_FEES_Python)

length = len(line1)
print('=' * length)
print(line1)
print(line2)
print('=' * length)
