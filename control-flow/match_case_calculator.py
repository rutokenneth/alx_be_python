num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = None

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1-num2
    case '*':
        result = num1*num2
    case '/':
        if num1 != 0:
            result = num1/num2
        else:
            print("Error: cannot divide by zero.")
    case _:
        print("Invalid operation")

if result is not None:
    print(f"The result is {result}")
