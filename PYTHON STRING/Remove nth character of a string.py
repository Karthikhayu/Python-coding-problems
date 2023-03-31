str = input("Enter the string: ")
str1 = ""
for i in range(0,len(str)):
    if i==3:
        continue
    else:
        str1 = str1 + str[i]
print (str1)