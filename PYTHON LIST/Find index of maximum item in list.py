list = [15,20,35,42,12,8]
max = list[0]
index = 0
for i in range(1,len(list)):
    if list[i] > max:
        max = list[i]
        index = i
print(f'Index of the maximum value is : {index}')