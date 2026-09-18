def check_admission(maths,physics,chemistry):
    total = maths + physics + chemistry

    if (maths >=50 and physics >=45 and chemistry >=60) or (maths + physics >=120):
        return "Student is eligible for Admission"
    else:
        return "Student is not eligible for Admission"

maths = int(input("Enter marks of Maths:"))
physics = int(input("Enter marks of Physics:"))
chemistry = int(input("Enter marks of Chemistry"))

result = check_admission(maths,physics,chemistry)

print(result)