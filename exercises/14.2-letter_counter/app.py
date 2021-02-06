par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for i in par:
    if i.lower() in counts:
        counts[i.lower()] += 1
    elif i != " ":
        counts[i.lower()] = 1
print(counts)

