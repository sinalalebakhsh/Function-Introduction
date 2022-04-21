from math import factorial
import re


def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

# 9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
# 8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8

# 9! = ( ... (factoral 7) * factorial 8) * 9

def factorial(n):
    print( n )
    if n == 1:
            return 1
    return n * factorial(n-1)

print(factorial(5))
