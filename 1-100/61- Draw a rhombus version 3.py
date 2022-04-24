def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')
import_os()

def print_star_line(number_of_stars, total_stars):
    numbers_of_spaces = (total_stars - number_of_stars) // 2 
    print(' ' * numbers_of_spaces, end='')
    print('*' * number_of_stars)


def draw_rhombus(num):
    print('')
    for i in range(num):
        if i < num / 2:
            print_star_line((i*2+1), num)
        else:
            print_star_line(((num - i)*2-1), num)
    print('')


    # for i in range(num//2+1):    |--------\   A mindset
    #     print(i*2+1)             |--------/


    # for i in range(1, num, 2):  |--------\
    #     print(i)                |---------\ Another way
    # for i in range(0, num, 2):  |---------/
    #     print(num - i)          |--------/
        

draw_rhombus(9)



