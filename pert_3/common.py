list1 = list(map(int, input("Enter numbers for the first list, separated by spaces: ").split()))
list2 = list(map(int, input("Enter numbers for the second list, separated by spaces: ").split()))

common_elements = list(set(list1) & set(list2))

print(f"The common elements of {list1} & {list2} are {common_elements}")
