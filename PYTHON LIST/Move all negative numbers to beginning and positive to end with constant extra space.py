array = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
j = 0
for i in range(len(array)) :
  if (array[i] < 0) :
    temp = array[i]
    array[i] = array[j]
    array[j]= temp
    j = j + 1
print(array)

