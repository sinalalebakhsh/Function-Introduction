def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

def factorial_calculation(a):
    result = 1
    for calc in range(1,a+1):
       result *= calc
    return result

print(factorial_calculation(4))
 
