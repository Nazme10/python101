

print("Sorry, the deli has run out of pastrami.\n")
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'egg', 'pastrami', 'veggie']
finished_sandwiches = []



while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
