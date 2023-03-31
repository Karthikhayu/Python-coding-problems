s = input("Enter the string: ")
s = s.title()
s = s.split()
str = ""
for i in s:
    str += i[:-1]+i[-1].upper()+ " "
print(str)