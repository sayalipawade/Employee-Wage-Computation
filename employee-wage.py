import random
print("Welcome to Employee Wage Computation")

#Constants
WAGE_PER_HOUR=20
FULL_DAY_HOUR=8
IS_EMP_PRESENT=1
IS_EMP_PART_TIME=2
WORKING_DAYS=20
MAXIMUM_HOURS=100
FULL_HOURS=8
HALF_HOURS=4

#variables
emp_hours=0
emp_daily_wage=0
emp_monthly_wage=0
total_emp_hours=0
total_working_days=0
emp_dict={}

class Employee:

    #Checking employee is present,absent or part time
    def calculate_employee_wage(self):
        global emp_hours
        global emp_monthly_wage
        global total_emp_hours
        global total_working_days
        try:
            while total_emp_hours<=MAXIMUM_HOURS and total_working_days<=WORKING_DAYS:
                emp_check=random.randint(0,2)
                if emp_check==IS_EMP_PRESENT:
                    emp_hours=FULL_HOURS
                elif emp_check==IS_EMP_PART_TIME:
                    emp_hours=HALF_HOURS
            
                #Calculating Daily wage of employee
                emp_daily_wage=emp_hours*WAGE_PER_HOUR
            
                #Getting total employee hours
                total_emp_hours=total_emp_hours+emp_hours
                total_working_days=total_working_days+1
            
                #Storing day and daily wage in dictionary
                print("Day:Daily Wage")
                emp_dict={total_working_days:emp_daily_wage}
                print(emp_dict)

            #Calculating Monthly wage of employee
            emp_monthly_wage=total_emp_hours*WAGE_PER_HOUR
            print("Total salary of employee:",emp_monthly_wage)
            
        except NameError:
            print("Name error exception occured!!!")

#Creating object of Employee class
employee=Employee()

#Calling method by using class object
employee.calculate_employee_wage()