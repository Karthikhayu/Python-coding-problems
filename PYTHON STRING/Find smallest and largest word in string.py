str = "It is a cat"
word = str.split()
largest=smallest=word[0]
for i in range(0, len(word)):
    if len(largest) < len (word[i]):
        largest = word[i]
    if len(smallest) > len (word[i]):
        smallest = word[i]
print("The largest string is: ", largest)
print("The smallest string is: ", smallest)