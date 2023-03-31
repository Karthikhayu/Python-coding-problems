str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
str1 = str1.split()
str2 = str2.split()
str = []
for i in str1:
    if i in str2:
          str.append(i)
print(str)