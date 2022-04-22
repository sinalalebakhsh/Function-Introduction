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
 

def calc_min_max_sum_len(*args):
    minimom = args[0]
    maximom = args[0]
    sum_num = 0
    length = 0
    for i in args:
        if i < minimom:
            minimom = i
        if i > maximom:
            maximom = i
        sum_num += i
        length += 1
    return minimom, maximom, sum_num, length

minimom, maximom, sum_number, length = calc_min_max_sum_len(10,2,3,4,5,6,7,8,9,10,11,12,13,14)

print(f"mimimom number : {minimom}")
print(f"maximom number : {maximom}")
print(f"sum number : {sum_number}")
print(f"length number : {length}")

