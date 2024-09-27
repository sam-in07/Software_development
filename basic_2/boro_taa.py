
def find_biggg(a,b,c) :
    if a>=b and a>=c :
        return  a
    elif b>=c and b>=a :
        return b
    else :
        return  c






a  = int(input())
b = int(input())
c  = int(input())


boro_man = find_biggg(a,b,c)

print(f"boro ta ber korbeeee yeaaaa {boro_man}")
