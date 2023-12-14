class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    def assign_emp_department(self, new_department):
        self.emp_department = new_department
        return {"Employee Name": self.emp_name,
                "Employee ID": self.emp_id,
                "Salary": self.emp_salary,
                "Department": self.emp_department}
    
    def print_employee_details(self):
        return {"Employee Name": self.emp_name,
                "Employee ID": self.emp_id,
                "Salary": self.emp_salary,
                "Department": self.emp_department}
        
        # print(f"""
        #       Employee Name: {self.emp_name}
        #       Employee ID: {self.emp_id}
        #       Salary: {self.emp_salary}
        #       Department: {self.emp_department}
        #       """)


adams = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
jones = Employee("JONES", "E7499", 45000, "RESEARCH")
martin = Employee("MARTIN", "E7900", 50000, "SALES")
smith = Employee("SMITH", "E7698", 55000, "OPERATIONS")


# Point soal 1
# print(adams.print_employee_details())

# Point soal 2
print(adams.assign_emp_department("COMPUTER"))




