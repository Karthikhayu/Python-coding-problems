arr = [ 1, 3, 20, 4, 99, 0 ]
n = len(arr)
a=[]
if (n == 1) :
      a = 0
if (arr[0] >= arr[1]):
        a = 0
if (arr[n - 1] >= arr[n - 2]):
        a = n - 1
for i in range(1, n - 1):
    if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]):
        a.append(i)
print (max(a))