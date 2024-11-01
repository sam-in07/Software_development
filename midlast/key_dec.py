# key exsists in a dectionary

my_dict = {'name': "john", 'age': 25, 'city': 'ctg', 'weight': 60, "height": 5.2}
key_to_check = input("enter the key you want to check : ")


if key_to_check in my_dict :
    print(f"the key'{key_to_check}' existst in the the dictionary")
else :
    print(f"the key'{key_to_check}' doesnot existst in the the dictornay")
