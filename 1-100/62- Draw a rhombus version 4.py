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
    number_of_stars = None
    for i in range(num):
        if i < num / 2:
            number_of_stars = (i * 2 + 1)
        else:
            number_of_stars = ((num - i) * 2 - 1 ) 

        print_star_line(number_of_stars, num)
    print('')


    # for i in range(num//2+1):    |--------\   A mindset
    #     print(i*2+1)             |--------/


    # for i in range(1, num, 2):  |--------\
    #     print(i)                |---------\ Another way
    # for i in range(0, num, 2):  |---------/
    #     print(num - i)          |--------/
        
get_number_from_user = int(input('Enter number: '))

while get_number_from_user != 'finish':
    if get_number_from_user == 0:
        print('Zero!!')
        get_number_from_user = int(input('Enter number: '))
    elif get_number_from_user % 2 != 0:
        draw_rhombus(get_number_from_user)
        get_number_from_user = int(input('Enter number: '))
    elif get_number_from_user % 2 == 0:
        get_number_from_user += 1
        draw_rhombus(get_number_from_user)
        get_number_from_user = int(input('Enter number: '))
    else:
        get_number_from_user = int(input('Enter number: '))





