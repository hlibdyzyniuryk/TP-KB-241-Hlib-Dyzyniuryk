lst = [3, 1, 4]
print("Initial list:", lst)

lst.append(5)
print("append:", lst)

lst.extend([7, 8])
print("extend:", lst)

lst.insert(1, 10)
print("insert:", lst)

lst.remove(4)
print("remove:", lst)

lst.sort()
print("sort:", lst)

lst.reverse()
print("reverse:", lst)

copy_lst = lst.copy()
print("copy:", copy_lst)

lst.clear()
print("clear:", lst)
