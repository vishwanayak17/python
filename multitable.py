def multiplication_table(number, n):

    for i in range(1, n + 1):
        print(number, "x", i, "=", number * i)

    return "Table completed"


number = int(input("Enter Number: "))
n = int(input("Enter Range: "))

result = multiplication_table(number, n)

print(result)