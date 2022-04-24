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
    # list_of_nums = []
    minimom = args[0]
    maximom = args[0]
    sum_num = 0
    length = 0
    for i in args:
        list_of_nums.append(i)
        if i < minimom:
            minimom = i
        if i > maximom:
            maximom = i
        sum_num += i
        length += 1
    return minimom, maximom, sum_num, length

# print(f"mimimom: {minimom} maximom: {maximom} multiply: {sum_number} length:{length}")

list_of_nums = []
print(list_of_nums)
print(calc_min_max_sum_len(12,13,14,14,15,1,2,3,4,))
print(list_of_nums)
