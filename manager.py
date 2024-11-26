from employee import Employee
import csv
import os

def initialize_csv(filename="Employees.csv"):
    if not os.path.exists(filename):  # Check if the file already exists
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Employee #', 'Employee ID', 'Name', 'Position', 'Salary', 'E-mail']
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            thewriter.writeheader()  # Write the header only once

class EmployeeManager:
    emp_count = 0

    def __init__(self):
        self.employees = []  # List to store employee objects
        initialize_csv()  # Initialize the CSV with headers if not already present

    def add_employee(self):
        # Input employee information
        id = input("Enter Employee ID: ")
        for employee in self.employees:
            if employee.emp_id == id:
                print("This ID already exists!")
                print("------------------------------")
                return
        
        name = input("Enter Employee Name: ")
        position = input("Enter Employee's Position: ")

        # Validate salary input
        salary = input("Enter Employee's Salary: ")
        if salary.isdigit():  # Check if salary contains only digits
            salary = float(salary)  
        else:
            print("Invalid salary. Please enter a numeric value.")
            print("------------------------------")
            return 
        
        email = input("Enter Employee's Email: ")
        if not ('@' in email and '.' in email.split('@')[-1]):
            print("Invalid email format. Employee not added.")
            print("------------------------------")
            return 

        new_employee = Employee(id, name, position, salary, email)
        self.employees.append(new_employee)

        EmployeeManager.emp_count += 1
        with open('Employees.csv', 'a', newline='') as csvfile:
            fieldnames = ['Employee #', 'Employee ID', 'Name', 'Position', 'Salary', 'E-mail']
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            thewriter.writerow({
                'Employee #': EmployeeManager.emp_count,
                'Employee ID': id,
                'Name': name,
                'Position': position,
                'Salary': salary,
                'E-mail': email
            })
        
        print("Successfully Added!")
        print("------------------------------")

    def update_emp(self):
        id = input("Enter the ID of the employee to be updated: ")
        for employee in self.employees:
            if employee.emp_id == id:
                print("What do you want to update?")
                print("1. Name\n2. Position\n3. Salary\n4. Email\n5. All")
                choice = int(input("Choose from 1-5: "))
                if choice == 1:
                    n_name = input("Enter the new name: ")
                    employee.update_employee(name=n_name)
                elif choice == 2:
                    n_position = input("Enter the new position: ")
                    employee.update_employee(position=n_position)
                elif choice == 3:
                    n_salary = input("Enter the new salary: ")
                    employee.update_employee(salary=n_salary)
                elif choice == 4:
                    n_email = input("Enter the new email: ")
                    employee.update_employee(email=n_email)
                elif choice == 5:
                    n_name = input("Enter the new name: ")
                    n_position = input("Enter the new position: ")
                    n_salary = input("Enter the new salary: ")
                    n_email = input("Enter the new email: ")
                    employee.update_employee(name=n_name, position=n_position, salary=n_salary, email=n_email)
                else:
                    print("Invalid choice")
                    return
                
                # Update the CSV
                self.save_to_csv()
                print("Successfully updated!")
                print("------------------------------")
                return
        
        print("Employee ID not found!")
        print("------------------------------")

    def delete_employee(self):
        id = input("Enter the ID of the employee to be deleted: ")
        for employee in self.employees:
            if employee.emp_id == id:
                self.employees.remove(employee)
                self.save_to_csv()  # Update the CSV after deletion
                print("Successfully Deleted!")
                print("------------------------------")
                return

        print("Employee ID not found!")
        print("------------------------------")

    def search_employee(self):
        id = input("Enter the ID of the employee to be searched: ")
        for employee in self.employees:
            if employee.emp_id == id:
                print(employee.display_employee())
                print("------------------------------")
                return
        
        print("Employee ID not found!")
        print("------------------------------")

    def list_all_employees(self):
        print("Employees Info")
        print("------------------------------")
        for i, employee in enumerate(self.employees, start=1):
            print(f"Employee {i}:")
            print(employee.display_employee())
            print("------------------------------")

    def save_to_csv(self):
        """Rewrites the entire employee list into the CSV."""
        with open('Employees.csv', 'w', newline='') as csvfile:
            fieldnames = ['Employee #', 'Employee ID', 'Name', 'Position', 'Salary', 'E-mail']
            thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            thewriter.writeheader()
            for i, employee in enumerate(self.employees, start=1):
                thewriter.writerow({
                    'Employee #': i,
                    'Employee ID': employee.emp_id,
                    'Name': employee.name,
                    'Position': employee.position,
                    'Salary': employee.salary,
                    'E-mail': employee.email
                })
