#1. Дано ціле число (int). Визначити скільки нулів у цьому числі.
#Вариант 1
my_number = 400000214210

number_str = str(my_number)
count = number_str.count(str(0))
print(count)
#Вариант 2

inta = 4000002142140
stringa = str(inta)
new_list = []
for number in stringa:
    new_list.append(int(number))

print(new_list.count(0))

#2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

my_number = 1002000

stringa = str(my_number)
zero_numbers = len(stringa) - len(stringa.rstrip('0'))
print(zero_numbers)

# #3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

my_list_1 = [5,4,645,4,7,4]
my_list_2 = [7,4,2,6,7457,534]
my_result = []

for pair in range(len(my_list_1)):
    if pair % 2 == 0:
        my_result.append(my_list_1[pair])
for pair in range(len(my_list_2)):
    if pair % 2 == 0:
        my_result.append(my_list_2[pair])
print(my_result)

# #4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

my_list = [1,2,3,4]
new_list = my_list[1:] + [my_list[0]]
print(new_list)

#5 Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)
my_list = [1,2,3,4]
delete_element = my_list.pop(0)
my_list.append(delete_element)
print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)

my_str = "43 більше ніж 34 , але менше ніж 56"
elements = my_str.split()

elements_sum = False

for element in elements:
    if element.isdigit():
        elements_sum += int(element)

print(elements_sum)

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

my_list = [2,4,1,5,3,9,0,7]

new_list = []

for index in range(1, len(my_list)-1):
    if my_list[index] > my_list[index-1] + my_list[index + 1]:
        new_list.append(my_list[index])

count_new_list = len(new_list)
print(count_new_list)

# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.

my_list = [1, 2, 3, "11", "22", 33]

new_list = [stringa for stringa in my_list if type(stringa) == str]

print(new_list)

# #9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

my_str = 'bla 25 not 47 57 car car car'
new_list = []

unique_set = set(my_str)
for let in unique_set:
    if my_str.count(let) == 1:
        new_list.append(let)

print(new_list)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

my_str_1 = 'a1'
my_str_2 = 'gft1'

set1 = set(my_str_1)
set2 = set(my_str_2)

new_list = list(set1.intersection(set2))
print(new_list)

# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# # але в кожній ТІЛЬКИ З одного разу.
my_str1 = "aaaasdf1"

my_str2 = "asdfff2"

new_list = []

set1 = set(my_str1)
set2 = set(my_str2)

same_let = list(set1.intersection(set2))

for let in same_let:
    if my_str1.count(let) == 1 and my_str2.count(let) == 1:
        new_list.append(let)

print(new_list)

