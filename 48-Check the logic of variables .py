from re import A


def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

a = 2
b = a
b = 3
print(a, b)

c = [1,2,3]
d = c
d[0] = 5           # The list changes here.
print( c , '-> C')
print( d , '-> D')


