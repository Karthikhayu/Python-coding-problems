s = input("Enter the string: ")
l = ["a","e","i","o","u"]
str = " "
count = 0
for i in range (0, len(s)):
    if s[i] in l:
        str = str + s[i]
        count = count + 1
print(str)
print(count)