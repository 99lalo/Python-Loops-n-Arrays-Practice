def lyrics_generator(numbers):
    whole_line = ""
    counter = 0
    for i in numbers:
        if i == 1 and counter == 2:
            whole_line += "Drop the base !!!Break the base!!! "
        elif i == 1:
            whole_line += "Drop the base "
            counter += 1
        else:
            whole_line += "Boom "
    return whole_line

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))