from manager import EmployeeManager

def main():
    exit = 0
    choice = 0
    new_manager = EmployeeManager()

    while exit == 0:
        print("Choose an option")
        print("1. Add Employee")
        print("2. Update Employee by ID")
        print("3. Delete Employee by ID")
        print("4. Search Employee by ID")
        print("5. List all Employees")
        print("6. Exit")
        print("------------------------------")
        choice = int(input("Choose: "))

        if choice == 1:
            new_manager.add_employee()
        elif choice == 2:
            new_manager.update_emp()
        elif choice == 3:
            new_manager.delete_employee()
        elif choice == 4:
            new_manager.search_employee()
        elif choice == 5:
            new_manager.list_all_employees()
        elif choice == 6:
            exit = 1 
            print("Successful Program Exit, Thank you!")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()