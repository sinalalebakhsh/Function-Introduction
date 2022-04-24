def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

list_names = ['sina', 'sina sinaiii', 'mina', 'mina tehrani', 'lina', 'lina saraii']

lambda list_by_map: len(list_by_map)

print(list(map(lambda list_by_map: len(list_by_map), list_names)))

print(list(map(lambda fullname : fullname.split()[0], list_names)))


