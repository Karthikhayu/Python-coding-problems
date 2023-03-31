s = input("Enter a string: ")
s = s.split()
str = ""
for i in range (len(s)):
    if i%2==0:
        str = str + s[i] + " "
    else:
        str = str + s[i][::-1] + " "
print(str)