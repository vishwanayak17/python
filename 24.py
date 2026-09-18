def check_num(number):
    if number < 0:
        return "Number is Negative" 
    elif number > 0:
        return "Number is Positive"
    else:
        return "Number is Zero" 

number = int(input("Enter a Number:"))
result = check_num(number)

print(f" {result}")