list1 = [[29, 13, 5, ], [1, 2, 3], [3, 9, 7, 4]]
list2 = [[100, 3], [9, 3, 5, 7], [6, 8]]
print("The original list 1 is : " + str(list1))
print("The original list 2 is : " + str(list2))
for i in range(0, len(list1)):
    list1[i].extend(list2[i])
print("The concatenated Matrix : " + str(list1))