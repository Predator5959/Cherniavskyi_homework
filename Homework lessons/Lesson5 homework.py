#рядок
value_str = 'Harry Potter and Python Lesson'
print(len(value_str))
#a. виведіть третій символ цього рядка.
print(value_str[2])
#b. виведіть передостанній символ цього рядка.
print(value_str[-2])
#c. виведіть перші п'ять символів цього рядка.
print(value_str[0:6])
#d. виведіть весь рядок, крім двох останніх символів
print(value_str[0:-2])
#e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи)
     #з першого).
print(value_str[0::2])
#f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
print(value_str[1::2])
#g. виведіть усі символи у зворотному порядку.
print(value_str[::-1])
#h.виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
print(value_str[::-2])
# i. виведіть довжину цього рядка.
print(len(value_str))
#2. Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів. Використовуйте для вирішення
#завдання функцію `count`
print(value_str.count(' ') + 1)
#3. Користувач вводить окремо рядок `s` та один символ `ch`. Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
#Для вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).

# s = input("Введіть рядок s: ")
# ch = input("Введіть символ ch: ")
#
# counter = 0
# index = s.find(ch)
#
# while index != -1:
#     counter += 1
#     print(f'Символ {ch} знайдено на позиції {index}')
#     index = s.find(ch, index + 1)
#
# if counter == 0:
#     print("Символ не знайдено")
# else:
#     print("Всього знайдено символів:", counter)




#4. Дано рядок. Замініть у цьому рядку всі появи літери `h` на літеру `H`, крім першого та останнього входження.
stringa = 'hello hey how hope house'
first = stringa.find('h')
print(first)
last = stringa.rfind('h')
print(last)
new_string = stringa[:first+1] + stringa[first+1:last].replace('h', 'H') + stringa[last:]
print(new_string)

my_string = '0123456789'

# for symbol1 in my_string:
#     for symbol2 in my_string:
#         num = int(symbol1 + symbol2)
#         print(num)
