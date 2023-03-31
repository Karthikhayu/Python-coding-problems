str = input("Enter the string: ")
s = ""
for i in str:
    if i not in s:
        s = s + i
print(s)