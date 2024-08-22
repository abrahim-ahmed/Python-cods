def calculator():
    x1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    x2 = float(input("Enter the second number: "))

    if operator == "+":
        result = x1 + x2
    elif operator == "-":
        result = x1 - x2
    elif operator == "*":
        result = x1 * x2
    elif operator == "/":
        result = x1 / x2
    else:
        print("Invalid!!")

    print("Result:", result)

calculator()
