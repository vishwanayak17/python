def gross_salary(basic):
    da = 30 * basic/100
    hra = 15 * basic/100
    pf = 12 * basic/100

    gross = basic + da + hra - pf
    return gross

basic = float(input("Enter Basic salary:"))
result = gross_salary(basic)

print("Gross Salary =", result)