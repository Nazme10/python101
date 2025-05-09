#Cities
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Calling function for three cities
describe_city("Reykjavik")           # Default country
describe_city("Akureyri")            # Default country
describe_city("Seoul", "South Korea") # Different country