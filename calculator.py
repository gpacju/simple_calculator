

def display_operations(operations):
    
    print()
    for op_num, op_name in operations.items():
        print(f'* {op_name} - {op_num}')


def perform_arithmetic_operations():

    operations = {'1': 'Addition',
                  '2': 'Subtraction',
                  '99': 'Quit'}

    welcome_msg = """
-------------------------------
Welcome to Simple Calculator!!!
-------------------------------

Simple Calculator can perform the below operations. 
Each arithmetic operation is mapped to a number.
"""

    print(welcome_msg)
    
    while True:

        display_operations(operations)

        op_input_msg = "Select the number of arithmetic operation to be performed : "

        op = input(op_input_msg).strip()
        
        if op not in operations:
            print(f'Selected invalid operation: {op}\nExiting ...')
            break
        elif op == '99':
            print(f'Quiting ...')
            break

        line = input('Enter two input numbers (x, y): ')
        n1, n2 = [int(n.strip()) for n in line.split(',')]

        if op == '1':
            result = n1 + n2
        elif op == '2':
            result = n1 - n2

        print(f'The result of {operations[op]} operation on two numbers, {n1} and {n1} is {result}')

        flag = input("Do you like to perform an other operation? (y/n): ")

        flag = flag.strip()
        if flag == 'n':
            print('Thank you for using Simple Calculator\nExiting ...')
            break
        elif flag == 'y':
            continue
        else:
            print(f'Provided invaild Input {flag}\nExiting ...')


if __name__ == '__main__':
    perform_arithmetic_operations()
    

