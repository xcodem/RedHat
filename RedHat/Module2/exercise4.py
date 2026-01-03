astring = input("Please enter some text: ")

firstchar = astring[0]
num_of_firstchar = astring.count(firstchar)

lastchar = astring[-1]
num_lastchar = astring.count(lastchar)

print("First character {0} occurs in the text {1} times.".format(firstchar, num_of_firstchar))

print("Last character {0} occurs in the text {1} times.".format(lastchar, num_lastchar))