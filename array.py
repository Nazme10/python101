# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
# person’s name.
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”


#3-1
names = ['Jui','Mimi','Summi','Zaheen','Ashfie']
print(type(names))
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


#3-2
print(f'Hello {names[0]}, How are you today?')
print(f'Hello {names[1]}, How are you today?')
print(f'Hello {names[2]}, How are you today?')
print(f'Hello {names[3]}, How are you today?')
print(f'Hello {names[4]}, How are you today?')

#3-3
cars = ['Mercedes','Bmw','Bentley']
print(f'I would like to own a {cars[0].upper()}.')
print(f'I would like to own a {cars[1].upper()}.')
print(f'I would like to own a {cars[2].upper()}.')

