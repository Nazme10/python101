result = {}

poll_active = True

while poll_active:
    name = input("Name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    result[name] = place

    repeat = input("Responding done.Next person?!(yes/no) ")
    if repeat.lower() == 'no':
        poll_active = False

print("\nPoll Results")
for name, place in result.items():
    print(f"{name} would like to go to {place}.")

