class Employee:
    def __init__(self,emp_name, emp_id, emp_salary,emp_department):  
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        
    def calculate_emp_salary(self, emp_salary):
        if hours_worked>50:
            overtime=hours_worked-50
            overtime_amount=(overtime*(salary/50))
            
    def emp_assign_department(self):
        self.emp_department=emp_department
    def print_employee_details(self):
        print("Name {}, ID {}, Salary {}, Department{}".format (self, self.emp_name, self.emp_id, self.emp_salary,self.emp_department))
        
print_=Employee("Adams","e000","5000","Sales")
print_.print_employee_details()
        
