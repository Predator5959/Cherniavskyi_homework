new_value = 40

result = new_value/2 if new_value < 100 else -new_value

print(result)

######################################################

new_value = 55

result = True if new_value < 100 else  False

print(result)


#####################################################


new_value = 55

result = True if new_value < 100 else  False

print(int(result))


#####################################################

my_str = 'qwer'

result = (my_str*2) if len(my_str) < 5 else (my_str)

print(str(result))

#####################################################

my_str = 'qwer'

result = (my_str + my_str[::-1]) if len(my_str) < 5 else (my_str)

print(str(result))
