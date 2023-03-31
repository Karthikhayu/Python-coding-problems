s = input('Enter the string: ')
sumd = 0
digit = ""
for i in range(0,len(s)):
    if (s[i].isdigit()):
        digit += s[i]
        sumd += int(s[i])
print("Original string: " , s)
print("Sum of digit: " , sumd)
print('Digit found in the string: ' , digit)    