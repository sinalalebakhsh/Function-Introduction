from re import A


def import_os():
    """ این تابع برای این هست که دیگه دو ایمپورت و دات سیستم رو ننویسی
     this function help lazy man :)))) 
     so you can use this :)))
     """
    import os
    os.system('cls')

import_os()

# a = 2
# b = a
# b = 3
# print(a, b)

# c = [1,2,3]
# d = c
# d[0] = 5           # The list changes here.
# print( c , '-> C')
# print( d , '-> D')

# e = [1,2,3]
# f = e
# f = [4,5,6]        # The list does not change here. Because you changed the whole list.
# print( e , '-> E')
# print( f , '-> F')

# def custom(a):
#     a = 2
#     print(a)
#     return a
# num = 100
# print(num)
# print(custom(num)) # don't change 
# print(num)


# def custom(list_name):
#     list_name.append('sina')

# example_list = [1, 2, 3, 4]
# print(example_list)
# custom(example_list) # The list change here <---------
# print(example_list)
def custom(a):
    copy_variable = a.copy()
    my_str = 'sina'
    copy_variable['bakhsh'] = my_str

my_dict = {
    'ky1' : 'lale'
}

print(my_dict)
custom(my_dict) # The dictionary change here
print(my_dict)
