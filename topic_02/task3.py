d = {"a": 1, "b": 2}
print("Initial dict:", d)

d.update({"c": 3})
print("update:", d)

print("keys:", list(d.keys()))
print("values:", list(d.values()))
print("items:", list(d.items()))

del d["a"]
print("del:", d)

d.clear()
print("clear:", d)
