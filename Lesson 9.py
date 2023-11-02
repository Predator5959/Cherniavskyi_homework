import random
import string
# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.

my_list = ['qwe', 'abc', 'gtx', 'wgf', 'sgrege']


def reverse_par_list(my_list):
    new_list = []
    for condition, item in enumerate(my_list):
        if condition % 2 == 0:
            new_list.append(item)
        else:
            new_list.append(item[::-1])
    return new_list

result = reverse_par_list(my_list)

print(result)

#2.Написати функцію яка приймає один параметр – список рядків my_list.
#Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".

my_list = ['qwe', 'abc', 'agtx', 'wgf', 'asarege']

def firs_word_a(my_list):
    new_list = [item for item in my_list if item.startswith('a')]
    return new_list

result = firs_word_a(my_list)
print(result)


# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

my_list = ['qwe', 'abc', 'agtx', 'wfggf', 'asarege', 'fdsfsdfdfa']

def include_word_a(my_list):
    new_list = [item for item in my_list if 'a' in item]
    return new_list

result = include_word_a(my_list)
print(result)

# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.

my_list = [1, 2, 3, "11", "22", 33]

def str_int_include(my_list):
    new_list = [stringa for stringa in my_list if type(stringa) == str]
    return new_list

result = str_int_include(my_list)
print(result)

# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.

my_str = 'bla 25 not 47 57 car car car'

def only_once_object(my_str):
    new_list = []
    unique_set = set(my_str)

    for let in unique_set:
        if my_str.count(let) == 1:
            new_list.append(let)
    return new_list

result = only_once_object(my_str)
print(result)

# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.

my_str_1 = 'a1'
my_str_2 = 'gft1'

def only_once_two_str(my_str_1,my_str_2):
    new_list = set(my_str_1).intersection(set(my_str_2))
    return new_list

result = list(only_once_two_str(my_str_1,my_str_2))
print(result)

#7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.

my_str1 = "aaaasdf1"
my_str2 = "asdfff2"

def same_laters_two_str(my_str1, my_str2):
    same_let = list(set(my_str1).intersection(set(my_str2)))
    new_list = []
    for let in same_let:
        if my_str1.count(let) == 1 and my_str2.count(let) == 1:
            new_list.append(let)
    return new_list

result = list(same_laters_two_str(my_str1,my_str2))
print(result)

# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

def create_email(domains, names):
    random_name = random.choice(names)
    random_number = random.randint(100,999)
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 7)))
    random_domain = random.choice(domains)
    email = f"{random_name}.{random_number}@{random_string}.{random_domain}"
    return email

e_mail = create_email(domains, names)
print(e_mail)