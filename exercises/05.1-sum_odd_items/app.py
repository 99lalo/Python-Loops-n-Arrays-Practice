arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

total = 0
for x in arr:
    if x%2 == 1:
        total += x
print(total)