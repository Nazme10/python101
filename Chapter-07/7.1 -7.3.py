rental_car = input("what kind of rental car would yoyu like?")
print(f"Let me see if I can find you a {rental_car}")


#7-2 
people = int(input("How many people are  there in your dinner group? "))

if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Table is ready!")

#7-3

number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")

