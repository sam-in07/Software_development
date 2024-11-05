def most_frequent_char(string):
    # Create a dictionary to store character frequencies
    char_count = {}
    
    # Count the frequency of each character in the string
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with the maximum frequency
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    return max_char, max_count

# Example usage
string = "example string with repeated characters"
most_frequent, frequency = most_frequent_char(string)
print(f"The most frequent character is '{most_frequent}' with a frequency of {frequency}.")