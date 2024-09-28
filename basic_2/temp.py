#temp calculaculator

def temp_calcu(a)  :
    b = (a*9/5)+32
    return  b



a = float(input())
#in celsius
farenhite  = temp_calcu(a)

print(f"{a} in celsius and farenhite = {farenhite}")
