def factorial_num(n):
    factorial = 1
    for i in range(1 , n+1 ):
        factorial = factorial * i

    return factorial 

n = int(input("Enter N:"))
result = factorial_num(n)

print("Factorial of given number =", result)