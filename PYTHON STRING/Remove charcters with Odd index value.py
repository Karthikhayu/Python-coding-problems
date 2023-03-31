i = input("Enter the string: " )
b = " "
for x in range(0, len(i)):
    if x%2==0:
        b += i[x]
print(b)