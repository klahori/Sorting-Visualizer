from random import randrange
# Generate random array
arr = []
size = 5
lower_bound = -15
upper_bound = 15
for i in range(size):
     arr.append(randrange(lower_bound, upper_bound + 1))

print("Orignial:", arr)
# Insertion Sort
