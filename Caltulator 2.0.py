error_number_only = 'please type only number'

while True:
    while True:
        try:
            number_1 = float(input('Please type the number'))
            #$if number_1 == int:
                #print('please type only number')
            break
        except ValueError:
            print(error_number_only)


    while True:
        zero_error = False
        try:
            number_2 = float(input('Please type the second number'))
            # if number_2 == int:
            #     print('please type only number')

        except ValueError:
            print(error_number_only)


        while True:

                oper = input('Please type operation : + - / *')

                if oper == '+':
                    result = number_1 + number_2

                elif oper == '-':
                    result = number_1 - number_2

                elif oper == '*':
                    result = number_1 * number_2



                elif oper == '/':
                    if number_2 == 0:
                        print("You can't divide by zero")
                        zero_error = True
                        break
                    result =  number_1 / number_2

                else:
                    print('please type next operators : + - / *')
                    continue
                print(result)
                break
        if zero_error:
            continue

        break

    again = input('Try again ? n = no. f = yes')
    if  again == 'n':
        break








