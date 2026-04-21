"""
Employee Management System module.
Handles all CRUD operations and data persistence.
"""

import json
import os
from datetime import datetime
from employee import FullTimeEmployee, PartTimeEmployee, ContractEmployee, Employee


class EmployeeManagementSystem:
    """
    Main system class for managing employees.
    Handles CRUD operations and file persistence.
    """
    
    def __init__(self, data_file='employees.json'):
        """Initialize the management system."""
        self.__employees = {}
        self.__data_file = data_file
        self.__load_employees()
    
    def add_employee(self, employee_type, emp_id, name, email, phone, department, salary, joining_date, **kwargs):
        """
        Add a new employee to the system.
        
        Args:
            employee_type: Type of employee ('fulltime', 'parttime', 'contract')
            emp_id: Employee ID
            name: Employee name
            email: Employee email
            phone: Employee phone
            department: Employee department
            salary: Employee salary
            joining_date: Employee joining date
            **kwargs: Additional arguments specific to employee type
        
        Returns:
            bool: True if employee added successfully, False otherwise
        """
        try:
            if emp_id in self.__employees:
                print(f"Error: Employee with ID {emp_id} already exists!")
                return False
            
            if employee_type.lower() == 'fulltime':
                benefits = kwargs.get('benefits', [])
                employee = FullTimeEmployee(emp_id, name, email, phone, department, salary, joining_date, benefits)
            
            elif employee_type.lower() == 'parttime':
                hours_per_week = kwargs.get('hours_per_week', 20)
                employee = PartTimeEmployee(emp_id, name, email, phone, department, salary, joining_date, hours_per_week)
            
            elif employee_type.lower() == 'contract':
                contract_end_date = kwargs.get('contract_end_date', '2025-12-31')
                employee = ContractEmployee(emp_id, name, email, phone, department, salary, joining_date, contract_end_date)
            
            else:
                print(f"Error: Unknown employee type '{employee_type}'")
                return False
            
            self.__employees[emp_id] = employee
            self.__save_employees()
            print(f"Employee {name} (ID: {emp_id}) added successfully.")
            return True
        
        except ValueError as e:
            print(f"Error adding employee: {e}")
            return False
    
    def update_employee(self, emp_id, **kwargs):
        """
        Update employee information.
        
        Args:
            emp_id: Employee ID to update
            **kwargs: Fields to update (name, email, phone, salary, department)
        
        Returns:
            bool: True if updated successfully, False otherwise
        """
        if emp_id not in self.__employees:
            print(f"Error: Employee with ID {emp_id} not found!")
            return False
        
        try:
            employee = self.__employees[emp_id]
            
            if 'name' in kwargs:
                employee.name = kwargs['name']
            if 'email' in kwargs:
                employee.email = kwargs['email']
            if 'phone' in kwargs:
                employee.phone = kwargs['phone']
            if 'salary' in kwargs:
                employee.salary = kwargs['salary']
            if 'department' in kwargs:
                employee.department = kwargs['department']
            
            self.__save_employees()
            print(f"Employee {emp_id} updated successfully.")
            return True
        
        except ValueError as e:
            print(f"Error updating employee: {e}")
            return False
    
    def delete_employee(self, emp_id):
        """
        Delete an employee from the system.
        
        Args:
            emp_id: Employee ID to delete
        
        Returns:
            bool: True if deleted successfully, False otherwise
        """
        if emp_id not in self.__employees:
            print(f"Error: Employee with ID {emp_id} not found!")
            return False
        
        employee_name = self.__employees[emp_id].name
        del self.__employees[emp_id]
        self.__save_employees()
        print(f"Employee {employee_name} (ID: {emp_id}) deleted successfully.")
        return True
    
    def search_employee(self, search_term):
        """
        Search employees by ID, name, or department.
        
        Args:
            search_term: Search term (ID, name, or department)
        
        Returns:
            list: List of matching employees
        """
        results = []
        search_term_lower = search_term.lower()
        
        for emp_id, employee in self.__employees.items():
            if (str(emp_id).lower() == search_term_lower or
                employee.name.lower().find(search_term_lower) != -1 or
                employee.department.lower().find(search_term_lower) != -1):
                results.append(employee)
        
        return results
    
    def get_employee(self, emp_id):
        """
        Get a specific employee by ID.
        
        Args:
            emp_id: Employee ID
        
        Returns:
            Employee: Employee object if found, None otherwise
        """
        return self.__employees.get(emp_id, None)
    
    def get_all_employees(self):
        """
        Get all employees.
        
        Returns:
            list: List of all employees
        """
        return list(self.__employees.values())
    
    def get_employees_by_department(self, department):
        """
        Get all employees in a specific department.
        
        Args:
            department: Department name
        
        Returns:
            list: List of employees in the department
        """
        return [emp for emp in self.__employees.values() 
                if emp.department.lower() == department.lower()]
    
    def deactivate_employee(self, emp_id):
        """
        Deactivate an employee.
        
        Args:
            emp_id: Employee ID
        
        Returns:
            bool: True if deactivated successfully, False otherwise
        """
        if emp_id not in self.__employees:
            print(f"Error: Employee with ID {emp_id} not found!")
            return False
        
        self.__employees[emp_id].deactivate()
        self.__save_employees()
        print(f"Employee {emp_id} has been deactivated.")
        return True
    
    def activate_employee(self, emp_id):
        """
        Activate an employee.
        
        Args:
            emp_id: Employee ID
        
        Returns:
            bool: True if activated successfully, False otherwise
        """
        if emp_id not in self.__employees:
            print(f"Error: Employee with ID {emp_id} not found!")
            return False
        
        self.__employees[emp_id].activate()
        self.__save_employees()
        print(f"Employee {emp_id} has been activated.")
        return True
    
    def get_active_employees(self):
        """
        Get all active employees.
        
        Returns:
            list: List of active employees
        """
        return [emp for emp in self.__employees.values() if emp.is_active]
    
    def get_inactive_employees(self):
        """
        Get all inactive employees.
        
        Returns:
            list: List of inactive employees
        """
        return [emp for emp in self.__employees.values() if not emp.is_active]
    
    def calculate_total_salary(self):
        """
        Calculate total salary for all active employees.
        
        Returns:
            float: Total salary
        """
        return sum(emp.salary for emp in self.get_active_employees())
    
    def calculate_total_bonus(self):
        """
        Calculate total bonus for all active employees.
        
        Returns:
            float: Total bonus
        """
        return sum(emp.calculate_bonus() for emp in self.get_active_employees())
    
    def __save_employees(self):
        """Save employees to JSON file."""
        try:
            data = {}
            for emp_id, employee in self.__employees.items():
                data[emp_id] = self.__employee_to_dict(employee)
            
            with open(self.__data_file, 'w') as f:
                json.dump(data, f, indent=4)
        
        except Exception as e:
            print(f"Error saving employees: {e}")
    
    def __load_employees(self):
        """Load employees from JSON file."""
        try:
            if os.path.exists(self.__data_file):
                with open(self.__data_file, 'r') as f:
                    data = json.load(f)
                
                for emp_id, emp_data in data.items():
                    employee = self.__dict_to_employee(emp_data)
                    if employee:
                        self.__employees[emp_id] = employee
        
        except Exception as e:
            print(f"Error loading employees: {e}")
    
    @staticmethod
    def __employee_to_dict(employee):
        """Convert employee object to dictionary."""
        emp_type = type(employee).__name__
        emp_dict = {
            'type': emp_type,
            'emp_id': employee.emp_id,
            'name': employee.name,
            'email': employee.email,
            'phone': employee.phone,
            'department': employee.department,
            'salary': employee.salary,
            'joining_date': employee.joining_date,
            'is_active': employee.is_active
        }
        
        if emp_type == 'FullTimeEmployee':
            emp_dict['benefits'] = employee.benefits
        elif emp_type == 'PartTimeEmployee':
            emp_dict['hours_per_week'] = employee.hours_per_week
        elif emp_type == 'ContractEmployee':
            emp_dict['contract_end_date'] = employee.contract_end_date
        
        return emp_dict
    
    @staticmethod
    def __dict_to_employee(emp_dict):
        """Convert dictionary to employee object."""
        emp_type = emp_dict.get('type')
        
        base_args = {
            'emp_id': emp_dict['emp_id'],
            'name': emp_dict['name'],
            'email': emp_dict['email'],
            'phone': emp_dict['phone'],
            'department': emp_dict['department'],
            'salary': emp_dict['salary'],
            'joining_date': emp_dict['joining_date']
        }
        
        try:
            if emp_type == 'FullTimeEmployee':
                employee = FullTimeEmployee(**base_args, benefits=emp_dict.get('benefits', []))
            elif emp_type == 'PartTimeEmployee':
                employee = PartTimeEmployee(**base_args, hours_per_week=emp_dict.get('hours_per_week', 20))
            elif emp_type == 'ContractEmployee':
                employee = ContractEmployee(**base_args, contract_end_date=emp_dict.get('contract_end_date', '2025-12-31'))
            else:
                return None
            
            if not emp_dict.get('is_active', True):
                employee.deactivate()
            
            return employee
        
        except Exception as e:
            print(f"Error creating employee from dict: {e}")
            return None
    
    def get_total_employees(self):
        """Get total number of employees."""
        return len(self.__employees)
    
    def display_statistics(self):
        """Display system statistics."""
        print("\n" + "="*60)
        print("EMPLOYEE MANAGEMENT SYSTEM - STATISTICS")
        print("="*60)
        print(f"Total Employees: {self.get_total_employees()}")
        print(f"Active Employees: {len(self.get_active_employees())}")
        print(f"Inactive Employees: {len(self.get_inactive_employees())}")
        print(f"Total Salary: ${self.calculate_total_salary():,.2f}")
        print(f"Total Bonus: ${self.calculate_total_bonus():,.2f}")
        print("="*60 + "\n")
