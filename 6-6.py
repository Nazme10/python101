
favorite_languages = {
    'mimi': 'python',
    'nazme': 'java',
    'jui': 'c++',
    'ash': 'js'
}

people = ['mimi', 'nazme', 'jui', 'ash', 'Sang Yan']
for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take the favorite languages poll!")
