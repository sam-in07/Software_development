#write  a program flatten nested loop

def check_empty_list(my_list) :
    if not my_list :
        return  " this list is empty"
    else :
      return "This list is  not empty"


user_list = []
print(check_empty_list(user_list))

user_list1 = [1,2,3]

print(check_empty_list(user_list1))
