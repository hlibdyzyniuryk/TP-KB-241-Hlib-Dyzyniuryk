my_dict = {"name": "Alex", "age": 20}
print("Initial dictionary:", my_dict)

my_dict.update({"city": "Kyiv"})
print("After update():", my_dict)

print("Keys:", my_dict.keys())

print("Values:", my_dict.values())

print("Items:", my_dict.items())

del my_dict["age"]
print("After del age:", my_dict)

my_dict.clear()
print("After clear():", my_dict)
