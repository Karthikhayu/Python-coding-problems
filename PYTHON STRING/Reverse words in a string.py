str = input("Enter the string: ")
str = str.split()
s = ""
for i in range(len(str)-1,-1,-1):
        s = s + str[i] + " "
print(s)