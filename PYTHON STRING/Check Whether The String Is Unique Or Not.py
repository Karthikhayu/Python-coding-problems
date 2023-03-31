s = "Karthik"
f = 0
str = " ".join(sorted(s))
print(s)
for i in range(0,len(str)-1):
    if (str[i]==str[i+1]):
        f=1
        break
if f==0:
    print("the string is unique")
else:
    print("the string is not unique")