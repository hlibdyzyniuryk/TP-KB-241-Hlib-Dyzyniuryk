import bisect

lst = [1, 3, 5, 7, 9]
print("Sorted list:", lst)

x = int(input("Enter number to insert: "))
pos = bisect.bisect_left(lst, x)

print(f"Element {x} should be inserted at position {pos}")
lst.insert(pos, x)

print("List after insertion:", lst)