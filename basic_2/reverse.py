'''
writer : sam__in07
time : 9:09 am

'''

#3reverse   numsss





num = int(input())
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
