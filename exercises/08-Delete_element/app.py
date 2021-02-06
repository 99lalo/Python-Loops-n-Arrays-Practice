people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    new_list = people[:]
    for name in new_list:
        if name == person_name:
            new_list.remove(str(person_name))
    return new_list
    #Your code go here:
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))