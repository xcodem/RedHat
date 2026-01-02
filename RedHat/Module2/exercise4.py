astring = input("Please enter some text: ")

firstchar = astring[0]
num_of_firstchar = astring.count(firstchar)

print("First character {0} occurs in the text {1} times.".format(firstchar, num_of_firstchar))
