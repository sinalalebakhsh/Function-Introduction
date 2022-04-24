def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

list_full_names = ['sina lalebakhsh', 'mina tehrani', 'mahsa shirazi', 'kimia mashhadi']

# Function for get first names:
def extract_first_names(list):
    return list.split()[0]
print(extract_first_names(list_full_names[0]))

# First way:
print(list(map(extract_first_names, list_full_names)))

# Second way:
list_first_names = []
for full_name in list_full_names:
    list_first_names.append(extract_first_names(full_name))
    print(extract_first_names(full_name))
print(list_first_names)







