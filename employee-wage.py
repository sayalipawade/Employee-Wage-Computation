import random
print("Welcome to Employee Wage Computation")

#Constants
WAGE_PER_HOUR=20
FULL_DAY_HOUR=8
IS_EMP_PRESENT=1
IS_EMP_PART_TIME=2
WORKING_DAYS=20

#variables
emp_hours=0
emp_daily_wage=0
emp_monthly_wage=0

class Employee:

    #Checking employee is present,absent or part time
    def checking_emp_attendance(self):
        global emp_hours
        global emp_monthly_wage
        for day in range(0,WORKING_DAYS):
            emp_check=random.randint(0,2)
            if emp_check==IS_EMP_PRESENT:
                emp_hours=8
            elif emp_check==IS_EMP_PART_TIME:
                emp_hours=4
            
            #Calculating daily wage of employee
            emp_daily_wage=emp_hours*WAGE_PER_HOUR
            #Calculating monthly wage of employee
            emp_monthly_wage=emp_monthly_wage+emp_daily_wage
        print("Employee Monthly wage:",emp_monthly_wage)

#Creating object of Employee class
employee=Employee()

#Calling method by using class object
employee.checking_emp_attendance()