# 1) У вас є список my_list із значеннями типу int. Роздрукувати значення, які більше 100.
#    Завдання виконати за допомогою циклу for.

my_list = [25,54,76,125,355,490,27,594]

for hundred in my_list:
    if hundred >= 100:
        print(hundred)


# 2) У вас є список my_list зі значеннями типу int і порожній список my_results. Додати в my_results ті значення,
#    які більше 100. Роздрукувати список my_results. Завдання виконати за допомогою циклу for.


my_list1 = [25,54,76,125,355,490,27,594]

empty_list = []

for hundred in my_list1:
    if hundred >= 100:
        empty_list.append(hundred)
print(empty_list)


# #3) У вас є список my_list із значеннями типу int. Якщо my_list кількість елементів менше 2,
#    то в кінець додати значення 0. Якщо кількість елементів більша або дорівнює 2,
#    то додати суму останніх двох елементів. Кількість елементів у списку можна отримати за допомогою функції len(my_list)

my_list2 = [25,54,76,125,355,490,27,594]
# my_list2 = [594,]
if len(my_list2) < 2:
    my_list2.append(0)
else: my_list2.append(my_list2[-1] + my_list2[-2])
print(my_list2)
######################################

my_str="bla BLA car"
unique_ch = set()
for char in my_str:
    unique_ch.add(char.lower())
print(len(unique_ch))
print(sorted(unique_ch))

###################
my_str = "bla BLA car"
empty_list = []

for pair in range(0, len(my_str), 2):
    empty_list.append(my_str[pair])
print(empty_list)

######################
my_str = "bla BLA car"
str_index = [0, 2, 4, 4, 8]
my_list = []

for index in str_index:
    if index < len(my_str):
        my_list.append(my_str[index])
print(my_list)

####################
numbers = 228989

num_str = str(numbers)
numbers_of_units = len(num_str)
print(numbers_of_units)

maximum = max(num_str, key=float)
print(float(maximum))

##########################
my_number = 123
print(str(my_number)[::-1])

###########################
my_number = 3254
sorted_num = int(''.join(sorted(str(my_number))))
print(sorted_num)
rev_sorted_num = int(''.join(sorted(str(my_number), reverse=True)))
print(rev_sorted_num)

############################
#A
my_list_1 = [1, 2, 3]
my_list_2 = [10, 20, 30]
my_result = []

for element in range(len(my_list_1)):
    my_result.append(my_list_1[element])
    my_result.append(my_list_2[element])

print(my_result)


########################

my_list_1 = [1, 2, 3]
my_list_2 = [10, 20, 30, 40]
my_result = []

min_len = min(len(my_list_1), len(my_list_2))

for element in range(min_len):
    my_result.append(my_list_1[element])
    my_result.append(my_list_2[element])

my_result.extend(my_list_1[min_len:])
my_result.extend(my_list_2[min_len:])

print(my_result)

