tea = ["green Tea","black Tea", "milk Tea","ginger Tea","red Tea","lemon Tea", "chamomile Tea"]
print(tea)
print()
#index
print(tea[2])
print()
#title func for cap
print(tea[5].title())
print()
#for printing last item use index [-1]
print(tea[-1])
#print second last
print(tea[-2])
print()
#Using Individual Values from a List
print(f"{tea[3].title()} is good for cold.")
print()
#modifying an element
tea[1]= "ginseng tea"
print(tea)
print()
#####  Adding Elements to a List
#adding new element to the end of the list using append() func
tea.append('ginger tea')
print(tea)
print()
#adding new element anywhere in the list using insert() func
tea.insert(4, 'herbal tea')
print(tea)
print()
#######  Removing Elements from a List
#remove using del() statement
del tea[4]
print(tea)
print('Last theke remove krar jnno pop() fuction use kra jabe')
expensive_tea = tea.pop()
print(f'{expensive_tea.title()} is pricey')
print()
#Popping Items from any Position in a List
print(tea.pop(0))
print(tea)
print()
#Removing an Item by Value
tea.remove("red Tea")
print(tea)
print()
####  organizing a list
#alphabetical order e sorting
print("ei way gulo te permanently change hbe")
tea.sort()
print(tea)
print("in reverse:", tea.sort(reverse=True))

#temporarily change krte sorted() func use krbo
print(sorted(tea))

#printing list in reverse order
tea.reverse()
#length
print(len(tea))
