def map_lists_to_dict(keys, values):
    # Initialize an empty dictionary
    result = {}
    
    # Iterate over the indices of the keys list
    for i in range(len(keys)):
        # Assign each key-value pair to the dictionary
        result[keys[i]] = values[i]
    
    return result

# Example usage
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

result = map_lists_to_dict(keys, values)
print(result)