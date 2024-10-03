'''
writer : sam__in07
time : 9:09 am

'''

#find second largest element

numbers_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
numbers_list.sort(reverse=True)
print(f"The ordered number list is = {numbers_list}")

