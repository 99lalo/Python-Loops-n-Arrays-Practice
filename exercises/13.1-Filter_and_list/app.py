
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filtering(ar):
    for a in ar:
        if a[0] == "R":
            return True
        else:
            return False
            
resulting_names = list(filter(filtering,all_names))
print(resulting_names)




