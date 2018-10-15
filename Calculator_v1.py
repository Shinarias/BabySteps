def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mul(number1, number2):
    return number1 * number2

def div(number1, number2):
    return number1 / number2


def main():

    validInput = False

    while not validInput:
        try:
            num1 = int(input("First number ? "))
            num2 = int(input("Second number ? "))
            operation = input("What do you want to do ? (add, mul, sub, div) ")
            validInput = True
        except:
            print("Invalid input, try again")

    if (operation == 'add'):
        print("Result: " + str(add(num1, num2)))
    elif (operation == 'sub'):
        print("Result: " + str(sub(num1, num2)))
    elif (operation == 'mul'):
        print("Result: " + str(mul(num1, num2)))
    elif (operation == 'div'):
        print("Result: " + str(div(num1, num2)))


main()