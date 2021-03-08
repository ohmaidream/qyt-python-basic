department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = "Department1 name:%-11sManager:%-11sCOURSE FEES:%-11.2fThe End!" \
        % (department1, depart1_m, COURSE_FEES_SEC)
line2 = "Department1 name:%-11sManager:%-11sCOURSE FEES:%-11.2fThe End!" \
        % (department2, depart2_m, COURSE_FEES_Python)

length = len(line1)
print('=' * length)
print(line1)
print(line2)
print('=' * length)


# line1 = '{0:<30} {1:<20} {2:<25} {3:8}'.format('"Department1 name:', 'Manager:', 'COURSE FEES:', 'The End!')
# print(line1)