def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

list_numbers_org = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def changer_to_even(list):
    if list % 2 != 0:
        return list + 1 
    else:
        return list

print(list(map(changer_to_even, list_numbers_org)))




