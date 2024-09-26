
def tringgoo(a,b,c) :
    s = (a+b+c)/2
    if a**2 == b**2+c**2 :
      return 0.5*b*c
    else :
        return (s*(s-a)*(s-b)*(s-c))



a = int(input())
b = int(input())
c = int(input())

result = tringgoo(a,b,c)

print(result)
