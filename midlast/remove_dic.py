#  remove key   a dectionary
my_dict = {'name': "john", 'age': 25, 'city': 'ctg', 'weight': 60, "height": 5.2}
key_to_remove = input("enter the key you want to check : ")


if key_to_remove in my_dict :
    remove = my_dict.pop(key_to_remove)
    print(f"the key'{key_to_remove}' remove with value {remove} from the the dictionary")
    print(f"updated dictonary = {my_dict}")
else :
    print(f"the key'{key_to_remove}' doesnot existst in the the dictornay")
