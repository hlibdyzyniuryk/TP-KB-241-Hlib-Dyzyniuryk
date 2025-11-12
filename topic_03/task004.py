def find_insert_position(sorted_list, new_value):
    for i in range(len(sorted_list)):
        if new_value < sorted_list[i]:
            return i
    return len(sorted_list)

nums = [1, 3, 5, 7, 9]
print("Sorted list:", nums)

new_num = int(input("Enter a number to insert: "))
position = find_insert_position(nums, new_num)
print(f"The new number should be inserted at index {position}.")
