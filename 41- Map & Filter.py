def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

list_number_org = [1, 2, 3, 4, 5, 6]

result_list = []

# The first way to achieve this goal :
# for num in list_number_org:
#     print(num ** 2 , end=' | ' )
#     result_list.append(num ** 2 )
# print('')

# We do not always need to do this
# The second way to achieve this goal: 
def power_two(num):
    return num ** 2

# for num in list_number_org:
#     print(power_two(num), end=' | ')
# print('')

# The third way to achieve this goal :
# map(power_two, list_number_org)

# We can not access this object with the print function
# print(map(power_two, list_number_org))  # output : <map object at 0x0000019D5D8FFFD0>

# but how can access to this object ? 
# First way to access object MAP:
# for num in map(power_two, list_number_org):
#     print(num, end=' | ')
# print('')

# Second way to access object MAP
# print(list(map(power_two, list_number_org)))

# Third way to access object MAP:
# third_way_to_access = list(map(power_two, list_number_org))
# print(third_way_to_access)

# Example for mulitpy numbers with object MAP:
def multiply_numbers(num):
    return num + 1
print(list(map(multiply_numbers, list_number_org)))



