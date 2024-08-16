first_number = int(input('type first number: '))
second_number = int(input('type second number: '))
operator = str(input('type operator: '))


with open('calculator_result.txt' , 'w') as file:
    file.write(f'the first number is {first_number} \n')
    file.write(f'the second number is {second_number} \n')
    file.write(f'the operator is {operator} \n')


def plus(a , b):
    result = (a + b)
    with open('calculator_result.txt' , 'w') as file:
        file.write(f'the first number is {first_number} \n')
        file.write(f'the second number is {second_number} \n')
        file.write(f'the operator is {operator} \n')
        file.write(f'result is {result}')


def minus(a , b):
    result = (a - b)
    with open('calculator_result.txt' , 'w') as file:
        file.write(f'the first number is {first_number} \n')
        file.write(f'the second number is {second_number} \n')
        file.write(f'the operator is {operator} \n')
        file.write(f'result is {result}')


def deleniye(a , b):
    result = (a / b)
    with open('calculator_result.txt' , 'w') as file:
        file.write(f'the first number is {first_number} \n')
        file.write(f'the second number is {second_number} \n')
        file.write(f'the operator is {operator} \n')
        file.write(f'result is {result}')

def umnojeniye(a , b):
    result = (a * b)
    with open('calculator_result.txt' , 'w') as file:
        file.write(f'the first number is {first_number} \n')
        file.write(f'the second number is {second_number} \n')
        file.write(f'the operator is {operator} \n')
        file.write(f'result is {result}')
try:
    if operator == '+':
        plus(first_number , second_number)
    elif operator == '-':
        minus(first_number , second_number)
    elif operator == '/':
        deleniye(first_number , second_number)
    elif operator == '*':
        umnojeniye(first_number , second_number)
except ValueError:
    print('please type numbers')
except ZeroDivisionError:
    print('the 0 not dividing ')