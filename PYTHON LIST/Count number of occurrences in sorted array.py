array = [1, 2, 2, 2, 2, 3, 4, 2 ,8 ,8]
x = 2 
g = 0
for i in range (len(array)):
    if x == array[i]:
        g = g + 1
print ("No of occurence is: ", g )  