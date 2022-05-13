num1= float(input("Enter the first Number format # + x = #: "))

op = input("Enter the operator: ")

num2= float(input("Enter the 3nd Number # + x = #: "))

answer = 0
match op:
    case "+":
        answer = num2 - num1
    case "-":
        answer = num2 + num1
    case "*":
        answer = num2 / num1
    case "/":
        answer = num2 * num1

        raise ValueError("Invalid Operator.")
print(f"x = {answer}")
