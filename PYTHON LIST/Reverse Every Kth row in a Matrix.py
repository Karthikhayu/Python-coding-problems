test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2],[3, 6], [3, 7, 4], [2, 9]]
print("The original list is : " + str(test_list))
K = 2
for i in range(K-1, len(test_list), K):
    test_list[i] = test_list[i][::-1]
print("After reversing every Kth row: " + str(test_list))