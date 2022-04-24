from pprint import pprint


def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()
 
def draw_rhombus(num):
    for i in range(num):
        if i < num / 2:
            print((i*2+1) * '*')
        else:
            print(((num - i)*2-1) * '*')


    # for i in range(num//2+1):    |--------\   A mindset
    #     print(i*2+1)             |--------/


    # for i in range(1, num, 2):  |--------\
    #     print(i)                |---------\ Another way
    # for i in range(0, num, 2):  |---------/
    #     print(num - i)          |--------/
        

draw_rhombus(9)



