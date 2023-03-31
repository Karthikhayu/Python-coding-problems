str = input("Enter the string: " )
s = str.split()
str1 = ""
for i in range(0,len(s)):
    str1 += s[i] + " "
print('String with extra spaces: ', str)
print('String without extra spaces: ', str1)