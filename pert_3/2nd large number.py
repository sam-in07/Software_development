'''
writer : sam__in07
time : 9:09 am

'''

#find second largest element

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return "There is no second largest number"
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

numbers_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
second_largest = find_second_largest(numbers_list)
print("The second largest number is:", second_largest)
