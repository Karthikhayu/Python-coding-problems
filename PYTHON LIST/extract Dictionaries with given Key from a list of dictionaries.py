list = [{'kk': 2, 'is': 8, 'good': 3},{'kk': 1, 'for': 10, 'me': 9},{'rpk': 3}]
print("The original list is : " + str(list))
key = 'kk'
result = [sub for sub in list if key in list(sub.keys())]
print("The filtered Dictionaries : " + str(result))