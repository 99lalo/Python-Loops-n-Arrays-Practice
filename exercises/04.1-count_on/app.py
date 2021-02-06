
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
for l in my_list:
    if type(l) is list or type(l) is dict:
        hello.append(l)
print(hello)
