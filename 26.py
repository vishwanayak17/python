def check_leap(year):
    if (year % 400 == 0 ) or (year % 4 ==0 and year % 100 != 0):
        return "Leap Year"
    else:
        return "Not Leap Year"

year = int(input("Enter Year:"))
result = check_leap(year)

print(f"{result}")