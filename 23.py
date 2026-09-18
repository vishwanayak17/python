def max_num(num1 ,num2):
    if (num1 > num2):
        return num1
    else:
        return num2

num1 = float(input("Enter Number1:"))
num2 = float(input("Enter Number2:"))

result = max_num(num1,num2)
print(f"Maximum Number is : {result}")