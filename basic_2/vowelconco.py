'''
writer : sam__in07
time : 9:09 am

'''

import random
def cntter(s) :
    vowel = "aeiouAEIOU"
    cnt = 0
    for i in s :
        if i in vowel :
            cnt+= 1
    return cnt




s = input()

vowel_cnt = cntter(s)

conso_cnt = len(s) - vowel_cnt
print(f"here is consonent number is {vowel_cnt} and vowel number is {conso_cnt}")
