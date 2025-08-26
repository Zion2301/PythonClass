#practising dictionaries
person = {"name": "Favour", "city": "Lagos", "age": 19}

# for key in person:
#     print(key, "->", person[key])

# Better way
for key, value in person.items():
    print(key, ":", value)
