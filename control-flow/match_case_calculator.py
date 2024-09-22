# Ask the user to input two numbers (one at a time)
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operation = (input("Choose the operation (+, -, *, /): "))

match operation:
    case "+":
        result = num1 + num2
        print (f"the result is", result,".")
    case "-":
        result = num1 - num2
        print (f"the result is", result,".")
    case "*":
        result = num1 *num2
        print (f"the ruesult is", result,".")
    case "/":
        if num2 == 0:
            print (f"cannot devide by zero")
        else:
            result = num1 / num2
            print (f"The result is [result].")
    case _:
        print (f"invalid operation entered.")