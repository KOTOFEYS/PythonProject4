calls = 0
def count_calls(func):
    def wrapper(*args,**kwarg):
        global calls
        calls += 1
        print(f"Функция была вызвана {calls} раз(а)")
        return func(*args,**kwarg)
    return wrapper
@count_calls
def string_info():
    string1 = (((len('capybara')), 'capybara'.upper(), 'capybara'))
    string2 = (((len('armageddon')), 'armageddon'.upper(), 'armageddon'))
    print(string1)
    print(string2)
@count_calls
def is_contains():
    string = ('urban', ['ban', 'BaNaN', 'urban'])
    string_new = (list(string))
    str1 = (string_new[1:2])
    list1 = ' '.join(str(el) for el in str1)
    element_to_check = 'urban'
    is_present1 = element_to_check in list1

    list_to_serch = ('cycle', ['recycling', 'cyclic'])
    string_new = (list(list_to_serch))
    str2 = (string_new[1:2])
    list2 = ' '.join(str(el) for el in str2)
    element_to_check = 'cycle'
    is_present2 = element_to_check in list2
    print(is_present1)
    print(is_present2)




string_info()
string_info()
string_info()
is_contains()







