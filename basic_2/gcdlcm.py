
def find_gcd(a,b) :
    while b :
        a , b = b , a%b
    return a

def find_lcm(a,b) :
    return (a*b)//find_gcd(a,b)

a  = int(input())
b = int(input())
c  = int(input())


lol = find_gcd(a,b)
lol1 = find_lcm(a,b)
print(f"gcd korbeeee yeaaaa {lol}")
print(f"lcm korbeeee yeaaaa {lol1}")
