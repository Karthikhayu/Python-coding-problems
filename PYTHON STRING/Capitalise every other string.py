s = ("Enter the string: ")
s1 = ""
for i in range (0, len(s)):
    if i%2==0:
        s1 += s[i].upper()
    else:
        s1 += s[i].lower()
print(s1)
