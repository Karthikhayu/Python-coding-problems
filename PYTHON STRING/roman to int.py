dict={'I':1,'V':5,'C':100,'X':10,'M':1000,'L':50,'D':500}
str="MCMXCIV"
prev=0
cur=0
res=0
for i in range(len(str)-1,-1,-1):
    cur=dict[str[i]]
    if(cur<prev):
        res-=cur
    else:
        res+=cur
    prev=cur
print(str, "Roman to INteger value:", res)