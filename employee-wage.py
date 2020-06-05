import random
print("Welcome to Employee Wage Computation")

class Employee:
    def checking_emp_present_or_absent(self):
        emp_check=random.randint(0,1)
        if emp_check==1:
            print("Employee is present")
        else:
            print("Employee is absent")

employee=Employee()
employee.checking_emp_present_or_absent()