cont = 'n'
while cont == 'n':
    try:
        number_1 = float(input('Please type the number'))
        oper = input('Please type operation : + - / *')
        number_2 = float(input('Please type the second number'))

        if oper == '+':
            print(number_1 + number_2)
        elif oper == '-':
            print(number_1 - number_2)
        elif oper == '*':
            print(number_1 * number_2)
        elif oper == '/':
            print(number_1 / number_2)
        else:
            print('Error')
    except ValueError:
        print('please type only number')
    cont = input('please press n to try again')