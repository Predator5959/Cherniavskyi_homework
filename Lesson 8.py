# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.

my_list = ['qwe', 'abc', 'gtx', 'wgf', 'sgrege']

new_list = []
for condition, item in enumerate(my_list):
    if condition  % 2 == 0:
        new_list.append(item)
    else:
        new_list.append(item[::-1])

print(new_list)

# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".

my_list = ['qwe', 'abc', 'agtx', 'wgf', 'asarege']

new_list = [item for item in my_list if item.startswith('a')]

print(new_list)

# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.

my_list = ['qwe', 'abc', 'agtx', 'wagf', 'srege', 'aaaaa']

new_list = [item for item in my_list if 'a' in item]

print(new_list)

# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
# в) Порахувати середню вік усіх людей із початкового списку.

persons = [{"name": "John", "age": 15}, {"name": "Valery", "age": 25}, {"name": "Jack", "age": 15}, {"name": "Vlad", "age": 65}]
# A
min_age = min(person["age"] for person in persons)

min_age_list = []

for person in persons:
    if person['age'] == min_age:
        min_age_list.append(person['name'])
print(min_age_list)
#B
max_name = max(len(person['name']) for person in persons)

max_person_name = []

for person in persons:
    if len(person['name']) == max_name:
        max_person_name.append(person['name'])
print(max_person_name)
#c

total_age = sum(person['age'] for person in persons)

total_persons = len(persons)

middle_age = total_age/total_persons

print(middle_age)

# 5) Дано два словники my_dict_1 і my_dict_2.
# а) Створити список із ключів, які є в обох словниках.
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
my_dict_1 = {"key1": 1, "key2": 2, "key3": 3}
my_dict_2 = {"key4": 4, "key1": 5, "key3": 6}
#a
keys_list = [key for key in my_dict_1 if key in my_dict_2]

print(keys_list)

#b
keys_list = [key for key in my_dict_1 if key not in my_dict_2]

print(keys_list)

#c
new_dict = {key: my_dict_1[key] for key in my_dict_1 if key not in my_dict_2}

print(new_dict)

#d
new_dict = {}

for key, value in my_dict_1.items():
    if key in my_dict_2:
        new_dict[key] = [value, my_dict_2[key]]
    else:
        new_dict[key] = value

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        new_dict[key] = value

print(new_dict)