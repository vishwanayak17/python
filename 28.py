def day_name(day):
    if day == 1:
        return "Sunday"
    elif day ==2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return "Wednesday"
    elif day == 5:
        return "Thursday"
    elif day == 6:
        return "Friday"
    elif day == 7:
        return "Saturday"
    else :
        return "Invalid day"

day = int(input("Enter day number:"))
result = day_name(day)
print(f"Day is : {result}")