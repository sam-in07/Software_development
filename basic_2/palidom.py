#palindrom

def is_pali(a) :
 a = a.replace(" ","") .lower()
 #a = str(a)
 return a == a[::-1]
  ## start int kotote koto dhap (-1)




a = input()

if is_pali(a) :
    print(f"its a palindrome")
else :
    print(f"its not a palindrome")
