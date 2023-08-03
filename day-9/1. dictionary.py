# python dictionary
# dictionary is a collection of key-value pairs
person = {
    "key": "value",
    "name": "John Doe",
    "age": 25,
    "address": "New York",
}

#  print the value of key
# print(person["key"])
# print(person["name"])

person["email"] = "john@doe.com"
# print(person)

# create empty dictionary
empty = {}

# add items to empty dictionary
empty["first_item"] = "Milk"
empty["second_item"] = "Bread"
empty["third_item"] = "Eggs"

# print(empty)


# wipe-out a dictionary
# person = {}
# print(person)

# edit existing item in the dictionary
empty["first_item"] = "Suger"
# print(empty)

# print all key-values in the dictionary
for key, value in empty.items():
    print(f"{key} : {value}")
