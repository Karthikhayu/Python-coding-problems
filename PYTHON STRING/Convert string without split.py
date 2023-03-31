n = "hello how are you"
l = []
temp = " "
for i in n:
    if i == " ":
        l.append(temp)
        temp = ' '
    else:
        temp = temp + i       
l.append(temp)        
print (l)                  