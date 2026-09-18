def calculator(operator,num1,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1/num2
    else :
        return "Invalid Operator"

operator = (input("Enter Operator:"))
num1 = int(input("Enter Number1:"))
num2 = int(input("Enter Number2:"))

result = calculator(operator,num1,num2)
print(f"{result}")