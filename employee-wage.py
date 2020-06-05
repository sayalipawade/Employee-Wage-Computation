import random
print("Welcome to Employee Wage Computation")

#Constants
WAGE_PER_HOUR=20
FULL_DAY_HOUR=8
IS_EMP_PRESENT=1

#variables
emp_hours=0
emp_daily_wage=0

class Employee:
    def checking_emp_present_or_absent(self):
        global emp_hours
        emp_check=random.randint(0,1)
        if emp_check==IS_EMP_PRESENT:
            emp_hours=8
        emp_daily_wage=emp_hours*WAGE_PER_HOUR
        print("Employee Daily Wage:",emp_daily_wage)

employee=Employee()
employee.checking_emp_present_or_absent()