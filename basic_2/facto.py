import math

def check_facto(n) :
    result = 1
    for i in range(1 , n+1) :
        result *= 1

    return result






a  = int (input())
if a<0:
 print("alays gives neg ")

else :
    print(f"the facto of {a} ! is  = {check_facto(a)}")
