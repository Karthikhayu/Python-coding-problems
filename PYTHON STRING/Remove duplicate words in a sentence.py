str = input("Enter the string: " )
str1 = str.split()
str2 = []
for i in str1:
    if i not in str2:
        str2.append(i)
print(str2)