# A Simple Calculator
operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))

# now for the if statements
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Math Error")
    else:
        print(num1 / num2)
else:
    print(f"{operator} is an invalid operator.")