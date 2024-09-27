
def find_gcd(a,b) :
    while b :
        a , b = b , a%b
    return a 



a  = int(input())
b = int(input())
c  = int(input())


lol = find_gcd(a,b)

print(f"gcd korbeeee yeaaaa {lol}")
