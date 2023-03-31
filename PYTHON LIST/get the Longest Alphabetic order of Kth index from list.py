list = ["apple", "is", "best", "for", "human", "and", "healthy"]
print("The original list is : " + str(list))
K = 1
result = []
curr = list[:1]
for i in range(1, len(list)):
    if list[i][K] <= list[i - 1][K]:
        if len(curr) > len(result):
            result = curr
        curr = [list[i]]
    else:
        curr.append(list[i])
if len(curr) > len(result):
    result = curr
print("Longest increasing Alphabetic order : " + str(result))