s = input("Enter the string")
s = " " + s
print(s)
c = 0
str = ""
for i in range(0,len(s)):
    if s[i] == " ":
        str += s[i+1].upper()
        print(str)
        c = i + 2
        print(c)
    else:
        str  += s[c]
        print(str)
        c =c +1
        print(c)
    if c== len(s):
        break
print(str)