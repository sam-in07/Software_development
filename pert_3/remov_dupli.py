#write  a program remove duplicate
def   remove_dupli(a) :
    return list(set(a))

def remove_dupli_second(a) :
  unique_list = []
  for element in a :
      if element not in  unique_list :
          unique_list.append(element)
  return unique_list

user_list = list(map(int, input("enter number sepaately").split()))

result = remove_dupli(user_list)
result2 = remove_dupli_second(user_list)
print("list after remove duplicates : ", result)
print("list after remove duplicates : ", result2)
