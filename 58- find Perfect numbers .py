def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()
 

def finder_divisor(num):
    all_div = []
    for i in range(1, num+1):
        if num % i == 0:
            all_div.append(i)
    return all_div

def finder_perfect(num):
    return sum(finder_divisor(num)) - num    

user_input = int(input('Enter number: '))

while user_input != 0:
    print(finder_divisor(user_input))
    print(finder_perfect(user_input))
    user_input = int(input('Enter number: '))