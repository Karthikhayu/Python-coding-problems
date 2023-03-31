A = [3, 2, 1, 56, 10000, 167]
min=max=A[0]
for i in range(0, len(A)):
    if min > A[i]:
        min = A[i]
    if max < A[i]:
        max = A[i]
print("Maximum is: ", max)
print("Minimum is: ", min)