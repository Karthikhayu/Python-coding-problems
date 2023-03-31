str = input("Enter the string: ")
s = " "
for i in str:
    if i.isalnum():
        s = s + i
print(s)