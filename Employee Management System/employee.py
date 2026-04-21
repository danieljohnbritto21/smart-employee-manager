"""
Employee module containing Employee classes with OOP principles.
Implements inheritance, encapsulation, and polymorphism.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Employee(ABC):
    """
    Abstract base class for all employees.
    Implements encapsulation with private attributes.
    """
    
    # Class variable to track employee count
    employee_count = 0
    
    def __init__(self, emp_id, name, email, phone, department, salary, joining_date):
        """Initialize employee with private attributes."""
        self.__emp_id = emp_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__department = department
        self.__salary = salary
        self.__joining_date = joining_date
        self.__is_active = True
        Employee.employee_count += 1
    
    # Encapsulation: Getters
    @property
    def emp_id(self):
        """Get employee ID."""
        return self.__emp_id
    
    @property
    def name(self):
        """Get employee name."""
        return self.__name
    
    @property
    def email(self):
        """Get employee email."""
        return self.__email
    
    @property
    def phone(self):
        """Get employee phone."""
        return self.__phone
    
    @property
    def department(self):
        """Get employee department."""
        return self.__department
    
    @property
    def salary(self):
        """Get employee salary."""
        return self.__salary
    
    @property
    def joining_date(self):
        """Get employee joining date."""
        return self.__joining_date
    
    @property
    def is_active(self):
        """Get employee active status."""
        return self.__is_active
    
    # Encapsulation: Setters
    @name.setter
    def name(self, value):
        """Set employee name."""
        if value.strip():
            self.__name = value
        else:
            raise ValueError("Name cannot be empty")
    
    @email.setter
    def email(self, value):
        """Set employee email."""
        if "@" in value:
            self.__email = value
        else:
            raise ValueError("Invalid email format")
    
    @phone.setter
    def phone(self, value):
        """Set employee phone."""
        if len(value) >= 10:
            self.__phone = value
        else:
            raise ValueError("Invalid phone number")
    
    @salary.setter
    def salary(self, value):
        """Set employee salary."""
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be positive")
    
    def deactivate(self):
        """Deactivate employee account."""
        self.__is_active = False
    
    def activate(self):
        """Activate employee account."""
        self.__is_active = True
    
    @abstractmethod
    def calculate_bonus(self):
        """
        Abstract method for calculating bonus.
        Must be implemented by subclasses (Polymorphism).
        """
        pass
    
    @abstractmethod
    def get_job_title(self):
        """
        Abstract method for getting job title.
        Must be implemented by subclasses (Polymorphism).
        """
        pass
    
    def get_details(self):
        """Get employee details as dictionary."""
        return {
            'emp_id': self.__emp_id,
            'name': self.__name,
            'email': self.__email,
            'phone': self.__phone,
            'department': self.__department,
            'salary': self.__salary,
            'joining_date': self.__joining_date,
            'job_title': self.get_job_title(),
            'bonus': self.calculate_bonus(),
            'status': 'Active' if self.__is_active else 'Inactive'
        }
    
    def __str__(self):
        """String representation of employee."""
        return (f"ID: {self.__emp_id} | Name: {self.__name} | "
                f"Department: {self.__department} | Salary: ${self.__salary} | "
                f"Status: {'Active' if self.__is_active else 'Inactive'}")
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Employee({self.__emp_id}, {self.__name}, {self.__department})"


class FullTimeEmployee(Employee):
    """
    Full-time employee class inheriting from Employee.
    Implements polymorphism by overriding abstract methods.
    """
    
    def __init__(self, emp_id, name, email, phone, department, salary, joining_date, benefits):
        """Initialize full-time employee with benefits."""
        super().__init__(emp_id, name, email, phone, department, salary, joining_date)
        self.__benefits = benefits
    
    @property
    def benefits(self):
        """Get employee benefits."""
        return self.__benefits
    
    @benefits.setter
    def benefits(self, value):
        """Set employee benefits."""
        self.__benefits = value
    
    def calculate_bonus(self):
        """Calculate bonus for full-time employee (10% of salary)."""
        return self.salary * 0.10
    
    def get_job_title(self):
        """Get job title for full-time employee."""
        return "Full-Time Employee"
    
    def __str__(self):
        """String representation with additional info."""
        base_str = super().__str__()
        return f"{base_str} | Type: Full-Time | Benefits: {', '.join(self.__benefits)}"


class PartTimeEmployee(Employee):
    """
    Part-time employee class inheriting from Employee.
    Implements polymorphism by overriding abstract methods.
    """
    
    def __init__(self, emp_id, name, email, phone, department, salary, joining_date, hours_per_week):
        """Initialize part-time employee with hours per week."""
        super().__init__(emp_id, name, email, phone, department, salary, joining_date)
        self.__hours_per_week = hours_per_week
    
    @property
    def hours_per_week(self):
        """Get hours per week."""
        return self.__hours_per_week
    
    @hours_per_week.setter
    def hours_per_week(self, value):
        """Set hours per week."""
        if 0 < value <= 40:
            self.__hours_per_week = value
        else:
            raise ValueError("Hours per week must be between 1 and 40")
    
    def calculate_bonus(self):
        """Calculate bonus for part-time employee (5% of salary)."""
        return self.salary * 0.05
    
    def get_job_title(self):
        """Get job title for part-time employee."""
        return "Part-Time Employee"
    
    def __str__(self):
        """String representation with additional info."""
        base_str = super().__str__()
        return f"{base_str} | Type: Part-Time | Hours/Week: {self.__hours_per_week}"


class ContractEmployee(Employee):
    """
    Contract employee class inheriting from Employee.
    Implements polymorphism by overriding abstract methods.
    """
    
    def __init__(self, emp_id, name, email, phone, department, salary, joining_date, contract_end_date):
        """Initialize contract employee with contract end date."""
        super().__init__(emp_id, name, email, phone, department, salary, joining_date)
        self.__contract_end_date = contract_end_date
    
    @property
    def contract_end_date(self):
        """Get contract end date."""
        return self.__contract_end_date
    
    @contract_end_date.setter
    def contract_end_date(self, value):
        """Set contract end date."""
        self.__contract_end_date = value
    
    def calculate_bonus(self):
        """Calculate bonus for contract employee (0% - no bonus)."""
        return 0
    
    def get_job_title(self):
        """Get job title for contract employee."""
        return "Contract Employee"
    
    def __str__(self):
        """String representation with additional info."""
        base_str = super().__str__()
        return f"{base_str} | Type: Contract | End Date: {self.__contract_end_date}"
