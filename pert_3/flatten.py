#write  a program flatten nested loop
def flatten_nested_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_nested_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

# Example usage
nested_list = [7, [3], 4, [2, [3, 4], 5], 6, [], [7, 8]]
flattened = flatten_nested_list(nested_list)
print("Flattened list:", flattened)
