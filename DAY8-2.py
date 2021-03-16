list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]
#
# for x in list1:
#     if x in list2:
#         print(f"{x} in List1 and List2")
#     else:
#         print(f"{x} only in List1")

def compare_list(l1,l2):
    for x in l1:
        if x in l2:
            print(f"{x} in List1 and List2")
        else:
            print(f"{x} only in List1")

compare_list(list1,list2)
