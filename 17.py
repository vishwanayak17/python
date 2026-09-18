def right_digit(num):
    num = int(num)
    digit = num % 10
    return digit 

num = float(input("Enter number:"))
digit = right_digit(num)
print("Rightmost digit =",digit)

