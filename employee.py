class Employee:
    # Initialization for the class
    def __init__(self,id,name,position,salary,email):
        self.emp_id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email 

    def update_employee(self,name=None,position=None,salary=None,email=None): #IDs are constant
        # Check the data which should be updated and update its corresponding value
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if salary is not None:
            self.salary = salary
        if email is not None:
            self.email = email

    def display_employee(self):
        return(f"ID: {self.emp_id}\n" f"Name: {self.name}\n" f"Position: {self.position}\n" f"Salary: {self.salary}\n" f"E-mail: {self.email}")
    
    