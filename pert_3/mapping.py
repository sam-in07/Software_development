#write  a program to find occarence

user_list = list(map(int, input("enter number sepaately").split()))

element_count = {}

for element in user_list :
    if element in element_count :
        element_count[element] += 1
    else :
      element_count[element] =   1

for element , count in element_count.items() :
    print(f"elements {element} occurs {count} times ")
