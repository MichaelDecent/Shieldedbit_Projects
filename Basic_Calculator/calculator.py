"""This Module contains the main calculator function """
from operators import add, sub, mul, div, mod

def main():
    valid = 1
    while valid >= 1:
        data = input("Usage: <value1> <operator> <value2>\n")
        data_list = data.split(' ')

        if len(data_list) != 3:
            print("Invalid input. Please provide <value1> <operator> <value2>.")
            continue

        try:
            val1, ops, val2 = int(data_list[0]), data_list[1], int(data_list[2])
        except ValueError:
            print("Please enter an integer for value1 and value2.")
            continue   

        operators = {'+': add, '-': sub, '*': mul, '/': div, '%': mod}

        if ops in operators:
            output = operators[ops](val1, val2)
            print("Result:", output)
            valid = int(input("Press 0 to exit, or any other number to continue: "))
        else:
            print("Invalid operator. Please use one of '+', '-', '*', '/', or '%'.")

if __name__ == '__main__':
    main()