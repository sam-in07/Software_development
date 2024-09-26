
def prime_chek(a) :
  if a<=1 :
      return  False
  for i in range (2 , int(a**0.5)+1 ) :
      if a %i == 0:
          return False


        return True




a = int(input())
# b = int(input())
# c = int(input())

result = prime_chek(a)

if prime_chek(a) :
  print(f"{a} is   a prime number ")
else :
    print(f"{a} is not prime ")

