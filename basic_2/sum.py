'''
writer : sam__in07
time : 8:31 am

'''

import random
#sum of n


'''
def sum_of_n(n) :
    b = (n*(n+1))//2
    return  b










n = float(input())
#b = float(input())

if n > 0 :
    ans = sum_of_n(n)
    print(f"sum of n numbersss  is {ans}")
else :
    print(f"NO answer ")
'''

#solving by using a range



def sum_of_n(start , n ):
    sum = 0
    for i in range(start,n+1):
        sum += i

    return  sum
start = int(input())
n = int(input())

if start > 0 and  start <= n :
    ans = sum_of_n(start , n )
    print(f"sum of n numbersss  is {ans}")
else :
    print(f"NO answer ")
