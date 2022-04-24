def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

# In the map, you say return what you want to replace.
# Inside the Filter, you say return True to me if you want the output to be known.
#تووی map میگی اون چیزی که میخوای جای اون قرار بگیره رو return کن.
# داخل Filter ، میگی اگه میخوای تووی خروجی معلوم باشه به من True برگردون.


list_numbers_org = [11, 20, 10, 15, 14, 28, 18, 9, 14, 15, 16, 17, 18, 19, 20, 1, 12, 14, 14, 13, 12]

def find_over_15(list_by_filter):
    if list_by_filter >= 15:
        return list_by_filter
    else:
        return False

#this command doesn't show value by filter
print(filter(find_over_15, list_numbers_org)) 

#this command show to you
print(list(filter(find_over_15, list_numbers_org)))



