def swap_numbers(num1, num2):
    num1, num2 = num2, num1
    return num1, num2


num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))

num1, num2 = swap_numbers(num1, num2)

print("Number1 =", num1)
print("Number2 =", num2)