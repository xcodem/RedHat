name = input ("Please enter your name: ")
name = name.capitalize()

print(f"Hello, {name}!")

age = int(input(f"Please enter your age {name}: "))

roundyears = 10 - (age % 10)

nextage = age + roundyears

print("so in {0} years you will be {1}!".format(roundyears, nextage))
print("so in hexadecimal {0} years  is {1}!".format(nextage, hex(nextage)))

