"""
Main console application for Employee Management System.
Provides user interface for managing employees.
"""

from employee_management import EmployeeManagementSystem
from datetime import datetime
import sys


class EmployeeManagementApp:
    """Console application for Employee Management System."""
    
    def __init__(self):
        """Initialize the application."""
        self.ems = EmployeeManagementSystem()
        self.running = True
    
    def display_header(self):
        """Display application header."""
        print("\n" + "="*70)
        print(" "*15 + "EMPLOYEE MANAGEMENT SYSTEM")
        print(" "*20 + "(OOP in Python)")
        print("="*70 + "\n")
    
    def display_main_menu(self):
        """Display main menu."""
        print("\n" + "-"*70)
        print("MAIN MENU")
        print("-"*70)
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. View Employees by Department")
        print("7. Deactivate/Activate Employee")
        print("8. View Statistics")
        print("9. Exit")
        print("-"*70)
    
    def add_employee_menu(self):
        """Menu for adding employee."""
        print("\n" + "-"*70)
        print("ADD EMPLOYEE")
        print("-"*70)
        
        try:
            emp_id = input("Enter Employee ID: ").strip()
            
            # Check if ID already exists
            if self.ems.get_employee(emp_id):
                print(f"Error: Employee with ID {emp_id} already exists!")
                return
            
            name = input("Enter Employee Name: ").strip()
            if not name:
                print("Error: Name cannot be empty!")
                return
            
            email = input("Enter Email: ").strip()
            phone = input("Enter Phone Number: ").strip()
            department = input("Enter Department: ").strip()
            
            try:
                salary = float(input("Enter Salary: "))
                if salary <= 0:
                    print("Error: Salary must be positive!")
                    return
            except ValueError:
                print("Error: Invalid salary amount!")
                return
            
            joining_date = input("Enter Joining Date (YYYY-MM-DD): ").strip()
            
            print("\nEmployee Type:")
            print("1. Full-Time")
            print("2. Part-Time")
            print("3. Contract")
            emp_type_choice = input("Select Employee Type (1-3): ").strip()
            
            if emp_type_choice == '1':
                benefits_input = input("Enter Benefits (comma-separated, e.g., Health Insurance, Pension): ").strip()
                benefits = [b.strip() for b in benefits_input.split(',')] if benefits_input else []
                self.ems.add_employee('fulltime', emp_id, name, email, phone, department, salary, joining_date, benefits=benefits)
            
            elif emp_type_choice == '2':
                try:
                    hours = float(input("Enter Hours per Week: "))
                    self.ems.add_employee('parttime', emp_id, name, email, phone, department, salary, joining_date, hours_per_week=hours)
                except ValueError:
                    print("Error: Invalid hours!")
            
            elif emp_type_choice == '3':
                contract_end = input("Enter Contract End Date (YYYY-MM-DD): ").strip()
                self.ems.add_employee('contract', emp_id, name, email, phone, department, salary, joining_date, contract_end_date=contract_end)
            
            else:
                print("Error: Invalid employee type selection!")
        
        except Exception as e:
            print(f"Error: {e}")
    
    def view_all_employees(self):
        """Display all employees."""
        print("\n" + "-"*70)
        print("ALL EMPLOYEES")
        print("-"*70)
        
        employees = self.ems.get_all_employees()
        
        if not employees:
            print("No employees found!")
            return
        
        for idx, emp in enumerate(employees, 1):
            print(f"\n{idx}. {emp}")
            details = emp.get_details()
            print(f"   Job Title: {details['job_title']}")
            print(f"   Bonus: ${details['bonus']:,.2f}")
            print(f"   Status: {details['status']}")
    
    def search_employee_menu(self):
        """Menu for searching employee."""
        print("\n" + "-"*70)
        print("SEARCH EMPLOYEE")
        print("-"*70)
        
        search_term = input("Enter Employee ID, Name, or Department: ").strip()
        
        if not search_term:
            print("Error: Search term cannot be empty!")
            return
        
        results = self.ems.search_employee(search_term)
        
        if not results:
            print(f"No employees found matching '{search_term}'!")
            return
        
        print(f"\nFound {len(results)} employee(s):\n")
        for idx, emp in enumerate(results, 1):
            print(f"{idx}. {emp}")
            details = emp.get_details()
            print(f"   Job Title: {details['job_title']}")
            print(f"   Email: {details['email']}")
            print(f"   Phone: {details['phone']}")
            print()
    
    def update_employee_menu(self):
        """Menu for updating employee."""
        print("\n" + "-"*70)
        print("UPDATE EMPLOYEE")
        print("-"*70)
        
        emp_id = input("Enter Employee ID to Update: ").strip()
        employee = self.ems.get_employee(emp_id)
        
        if not employee:
            print(f"Error: Employee with ID {emp_id} not found!")
            return
        
        print(f"\nCurrent Details: {employee}")
        print("\nWhat would you like to update?")
        print("1. Name")
        print("2. Email")
        print("3. Phone")
        print("4. Department")
        print("5. Salary")
        print("6. Back to Main Menu")
        
        choice = input("Select option (1-6): ").strip()
        
        update_dict = {}
        
        try:
            if choice == '1':
                new_name = input("Enter new name: ").strip()
                update_dict['name'] = new_name
            elif choice == '2':
                new_email = input("Enter new email: ").strip()
                update_dict['email'] = new_email
            elif choice == '3':
                new_phone = input("Enter new phone: ").strip()
                update_dict['phone'] = new_phone
            elif choice == '4':
                new_dept = input("Enter new department: ").strip()
                update_dict['department'] = new_dept
            elif choice == '5':
                new_salary = float(input("Enter new salary: "))
                update_dict['salary'] = new_salary
            elif choice == '6':
                return
            else:
                print("Error: Invalid option!")
                return
            
            if update_dict:
                self.ems.update_employee(emp_id, **update_dict)
        
        except ValueError as e:
            print(f"Error: {e}")
    
    def delete_employee_menu(self):
        """Menu for deleting employee."""
        print("\n" + "-"*70)
        print("DELETE EMPLOYEE")
        print("-"*70)
        
        emp_id = input("Enter Employee ID to Delete: ").strip()
        employee = self.ems.get_employee(emp_id)
        
        if not employee:
            print(f"Error: Employee with ID {emp_id} not found!")
            return
        
        print(f"Are you sure you want to delete {employee.name}? (yes/no): ").strip()
        confirm = input().strip().lower()
        
        if confirm == 'yes':
            self.ems.delete_employee(emp_id)
        else:
            print("Operation cancelled!")
    
    def view_by_department_menu(self):
        """Menu for viewing employees by department."""
        print("\n" + "-"*70)
        print("VIEW EMPLOYEES BY DEPARTMENT")
        print("-"*70)
        
        department = input("Enter Department Name: ").strip()
        
        if not department:
            print("Error: Department name cannot be empty!")
            return
        
        employees = self.ems.get_employees_by_department(department)
        
        if not employees:
            print(f"No employees found in {department} department!")
            return
        
        print(f"\nEmployees in {department} Department:\n")
        for idx, emp in enumerate(employees, 1):
            print(f"{idx}. {emp}")
    
    def deactivate_activate_menu(self):
        """Menu for deactivating/activating employee."""
        print("\n" + "-"*70)
        print("DEACTIVATE/ACTIVATE EMPLOYEE")
        print("-"*70)
        
        emp_id = input("Enter Employee ID: ").strip()
        employee = self.ems.get_employee(emp_id)
        
        if not employee:
            print(f"Error: Employee with ID {emp_id} not found!")
            return
        
        status = "Active" if employee.is_active else "Inactive"
        print(f"Employee {employee.name} is currently {status}")
        
        if employee.is_active:
            action = input("Deactivate this employee? (yes/no): ").strip().lower()
            if action == 'yes':
                self.ems.deactivate_employee(emp_id)
        else:
            action = input("Activate this employee? (yes/no): ").strip().lower()
            if action == 'yes':
                self.ems.activate_employee(emp_id)
    
    def view_statistics(self):
        """Display system statistics."""
        self.ems.display_statistics()
        
        # Display employees by type
        print("\nEmployees by Status:")
        print("-" * 60)
        active = self.ems.get_active_employees()
        inactive = self.ems.get_inactive_employees()
        
        print(f"\nActive Employees ({len(active)}):")
        if active:
            for emp in active:
                print(f"  • {emp.name} - {emp.department}")
        else:
            print("  No active employees")
        
        print(f"\nInactive Employees ({len(inactive)}):")
        if inactive:
            for emp in inactive:
                print(f"  • {emp.name} - {emp.department}")
        else:
            print("  No inactive employees")
    
    def run(self):
        """Run the application."""
        self.display_header()
        
        while self.running:
            self.display_main_menu()
            
            try:
                choice = input("\nSelect option (1-9): ").strip()
                
                if choice == '1':
                    self.add_employee_menu()
                elif choice == '2':
                    self.view_all_employees()
                elif choice == '3':
                    self.search_employee_menu()
                elif choice == '4':
                    self.update_employee_menu()
                elif choice == '5':
                    self.delete_employee_menu()
                elif choice == '6':
                    self.view_by_department_menu()
                elif choice == '7':
                    self.deactivate_activate_menu()
                elif choice == '8':
                    self.view_statistics()
                elif choice == '9':
                    print("\n" + "="*70)
                    print("Thank you for using Employee Management System!")
                    print("="*70 + "\n")
                    self.running = False
                else:
                    print("Error: Invalid option! Please select from 1-9.")
            
            except KeyboardInterrupt:
                print("\n\nApplication interrupted by user.")
                self.running = False
            except Exception as e:
                print(f"Error: {e}")


def main():
    """Main entry point."""
    app = EmployeeManagementApp()
    app.run()


if __name__ == "__main__":
    main()
