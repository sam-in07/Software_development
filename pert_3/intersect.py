#write  a program intersect of two set

def find_intersection(set1, set2):
    myIntersection = set1.intersection(set2)
    return myIntersection

set_input1 = input("Enter elements of the first set, separated by spaces: ")
set_input2 = input("Enter elements of the second set, separated by spaces: ")

set1 = set(map(int, set_input1.split()))
set2 = set(map(int, set_input2.split()))

result = find_intersection(set1, set2)

print('Intersection of set1 and set2:', result)
