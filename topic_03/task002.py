my_list = [1, 2, 3]
print("Initial list:", my_list)

my_list.append(4)
print("After append(4):", my_list)

my_list.extend([5, 6])
print("After extend([5, 6]):", my_list)

my_list.insert(2, 99)
print("After insert(2, 99):", my_list)

my_list.remove(99)
print("After remove(99):", my_list)

my_list.sort()
print("After sort():", my_list)

my_list.reverse()
print("After reverse():", my_list)

new_list = my_list.copy()
print("Copy of list:", new_list)

my_list.clear()
print("After clear():", my_list)
