'''
writer : sam__in07
time : 9:09 am

'''

import string
def remove_punch(s):
    translator = s.maketrans(' ' , ' ' , string.punctuation)
    '''
      #maketrans has 3 part x y z   x = kare replace korbo   y = oi replace jaigie kare bosbabo y = kare dlt kormu
     #maketrans() kaj hocche bad deya 
    '''
    return  s.translate(translator)


s = input()

clean_str = remove_punch(s)


print(clean_str)
