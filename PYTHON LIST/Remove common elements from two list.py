list1 = [1, 2, 3, 4, 5]  
list2 = [4, 5, 6, 7, 8]
list3 = []
list4 = []
for i in list1:
    if i  not in list2:
        list3.append(i)
for j in list2:
     if j not in list1:
        list4.append(j)
print(list3)
print(list4)  