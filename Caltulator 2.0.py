while True:
    while True:
        try:
            number_1 = float(input('Please type the number'))
            if number_1 == int:
                print('please type only number')
            break
        except ValueError:
            print('please type only number')


    while True:
        try:
            number_2 = float(input('Please type the second number'))
            if number_2 == int:
                print('please type only number')
            break
        except ValueError:
            print('please type only number')


    while True:
        try:
            oper = input('Please type operation : + - / *')

            if oper == '+':
                print(number_1 + number_2)

            elif oper == '-':
                print(number_1 - number_2)

            elif oper == '*':
                print(number_1 * number_2)

            elif oper == '/':
                print(number_1 / number_2)

            break

        except ValueError:
             print('please type next operators : + - / *')








