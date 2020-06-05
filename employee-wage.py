import random
print("Welcome to Employee Wage Computation")

#Constants
WAGE_PER_HOUR=20
FULL_DAY_HOUR=8
IS_EMP_PRESENT=1
IS_EMP_PART_TIME=2

#variables
emp_hours=0
emp_daily_wage=0

class Employee:

    #Checking employee is present,absent or part time
    def checking_emp_attendance(self):
        global emp_hours
        emp_check=random.randint(0,2)
        if emp_check==IS_EMP_PRESENT:
            emp_hours=8
        elif emp_check==IS_EMP_PART_TIME:
            emp_hours=4
        emp_daily_wage=emp_hours*WAGE_PER_HOUR
        print("Employee Daily Wage:",emp_daily_wage)

#Creating object of Employee class
employee=Employee()

#Calling method by using class object
employee.checking_emp_attendance()