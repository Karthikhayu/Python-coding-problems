str = input("Enter the string: ")
str1 = ""
for i in str:
    if i>="0" and i<="9":
        continue
    else:
        str1 = str1 + i
print(str1)