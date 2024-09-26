import math

def is_fibo(n) :
    a = 0
    b = 1
    for _ in range(n) :
         print(a , end = ' ')
         nextTerm = a+b
         a =  b
         b = nextTerm








a = int(input())


if a<=0 :
    print("pls enter a positive int ")

else :
    print(f"the fibo series of {a} is = ")
    is_fibo(a)
