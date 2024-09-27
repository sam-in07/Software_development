#swaping values

def myswap(x , y)  :
    x , y = y , x
    return  x , y





a = int(input())
b = int(input())

#a , b = myswap(a,b)
res = myswap(a,b)
#print(f"after swap {a} and {b}")
print(res)
