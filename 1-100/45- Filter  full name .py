def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

list_names = ['sina', 'sina sinaiii', 'mina', 'mina tehrani', 'lina', 'lina saraii']

def show_full_name(list_by_filter):
    if ' ' in list_by_filter:
        return list_by_filter

print(list(filter(show_full_name, list_names)))


