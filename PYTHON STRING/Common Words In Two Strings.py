str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
a = str1.split()
b = str2.split()
s = []
for i in a:
    if i in b:
        s.append(i)
print(s)