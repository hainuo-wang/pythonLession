list1 = list(input().split(","))
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
