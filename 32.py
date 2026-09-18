def check_grade(marks):
    if marks >=0 and marks <= 34 :
        return "Fail"
    elif marks >= 35 and marks <= 59:
        return "Second class"
    elif marks >= 60 and marks <= 79:
        return "First class"
    elif marks >= 80 and marks <= 100:
        return "Dist"
    else:
        return "Invalid marks"

marks = int(input("Enter a marks:"))
result = check_grade(marks)

print("Grade =",result)