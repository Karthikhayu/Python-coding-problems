s = input("Enter the string: ")
str = " "
for i in range(len(s)):
    l = len(s)//2
    if i>=l :
        str = str+s[i].upper()
    else:
        str = str+s[i].lower()
print(str)