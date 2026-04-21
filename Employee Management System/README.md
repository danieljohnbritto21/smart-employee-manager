# Employee Management System (Python OOP)

A comprehensive console-based Employee Management System built with Object-Oriented Programming principles in Python.

## Features

### ✨ Core Features
- **Add Employees** - Add full-time, part-time, or contract employees
- **Update Employees** - Modify employee information
- **Delete Employees** - Remove employee records
- **Search Employees** - Find employees by ID, name, or department
- **View Employees** - Display all employees or by department
- **Deactivate/Activate** - Manage employee status
- **Statistics** - View system-wide statistics

### 🏗️ OOP Principles Implemented

#### 1. **Encapsulation**
- Private attributes with property decorators (getters/setters)
- Data validation through setters
- Protected access to sensitive data

```python
@property
def salary(self):
    return self.__salary

@salary.setter
def salary(self, value):
    if value > 0:
        self.__salary = value
    else:
        raise ValueError("Salary must be positive")
```

#### 2. **Inheritance**
- Base `Employee` abstract class
- Specialized employee types:
  - `FullTimeEmployee` - Includes benefits
  - `PartTimeEmployee` - Includes hours per week
  - `ContractEmployee` - Includes contract end date

```python
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, ..., benefits):
        super().__init__(emp_id, name, ...)
        self.__benefits = benefits
```

#### 3. **Polymorphism**
- Abstract methods in base class
- Different implementations in subclasses
- `calculate_bonus()` - Different bonus logic per type
- `get_job_title()` - Type-specific job titles

```python
class FullTimeEmployee(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10  # 10% bonus

class PartTimeEmployee(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05  # 5% bonus

class ContractEmployee(Employee):
    def calculate_bonus(self):
        return 0  # No bonus
```

#### 4. **Abstraction**
- Abstract base class using ABC
- Abstract methods enforce implementation in subclasses
- Complex logic hidden from user interface

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_bonus(self):
        pass
    
    @abstractmethod
    def get_job_title(self):
        pass
```

## Project Structure

```
Employee Management System/
├── employee.py                 # Employee classes with OOP principles
├── employee_management.py     # Management system (CRUD operations)
├── main.py                    # Console application interface
├── employees.json             # Data persistence file (auto-generated)
└── README.md                  # This file
```

## Installation

### Prerequisites
- Python 3.7+
- No external dependencies required

### Setup
```bash
# Navigate to the project directory
cd "Employee Management System"

# Run the application
python main.py
```

## Usage

### Running the Application
```bash
python main.py
```

### Menu Options

#### 1. Add Employee
- Select employee type (Full-Time, Part-Time, Contract)
- Enter employee details
- Add benefits, hours, or contract end date as applicable

#### 2. View All Employees
- Displays all employees with their details
- Shows job title, bonus, and status

#### 3. Search Employee
- Search by Employee ID
- Search by Name
- Search by Department

#### 4. Update Employee
- Modify employee information
- Update name, email, phone, department, or salary

#### 5. Delete Employee
- Remove employee records (with confirmation)

#### 6. View by Department
- Filter employees by department

#### 7. Deactivate/Activate
- Change employee status

#### 8. View Statistics
- Total employees count
- Active/Inactive count
- Total salary and bonus calculations

## Code Examples

### Creating Employees Programmatically

```python
from employee_management import EmployeeManagementSystem

# Initialize system
ems = EmployeeManagementSystem()

# Add Full-Time Employee
ems.add_employee(
    'fulltime',
    emp_id='E001',
    name='John Doe',
    email='john@example.com',
    phone='1234567890',
    department='IT',
    salary=50000,
    joining_date='2023-01-15',
    benefits=['Health Insurance', 'Pension']
)

# Add Part-Time Employee
ems.add_employee(
    'parttime',
    emp_id='E002',
    name='Jane Smith',
    email='jane@example.com',
    phone='9876543210',
    department='HR',
    salary=25000,
    joining_date='2023-02-20',
    hours_per_week=25
)

# Add Contract Employee
ems.add_employee(
    'contract',
    emp_id='E003',
    name='Bob Wilson',
    email='bob@example.com',
    phone='5555555555',
    department='Finance',
    salary=35000,
    joining_date='2023-03-10',
    contract_end_date='2024-12-31'
)

# Search employees
results = ems.search_employee('IT')

# Get statistics
print(f"Total Employees: {ems.get_total_employees()}")
print(f"Total Salary: ${ems.calculate_total_salary():,.2f}")
print(f"Total Bonus: ${ems.calculate_total_bonus():,.2f}")
```

## Data Persistence

Employee data is automatically saved to `employees.json` after each operation:

```json
{
    "E001": {
        "type": "FullTimeEmployee",
        "emp_id": "E001",
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "department": "IT",
        "salary": 50000,
        "joining_date": "2023-01-15",
        "benefits": ["Health Insurance", "Pension"],
        "is_active": true
    }
}
```

## OOP Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| **Classes** | Employee, FullTimeEmployee, PartTimeEmployee, ContractEmployee, EmployeeManagementSystem |
| **Objects** | Employee instances stored in management system |
| **Inheritance** | Employee subclasses inherit from base Employee class |
| **Encapsulation** | Private attributes with public property accessors |
| **Polymorphism** | Different bonus calculations and job titles per employee type |
| **Abstraction** | Abstract methods force implementation in subclasses |
| **Access Modifiers** | Private (__), public, protected attributes |
| **Class Variables** | employee_count tracking across all instances |
| **Methods** | Instance methods, class methods, static methods, abstract methods |

## Bonus Calculation

Different bonus rates apply to each employee type:

- **Full-Time Employee**: 10% of salary
- **Part-Time Employee**: 5% of salary  
- **Contract Employee**: 0% (no bonus)

## Error Handling

The system includes comprehensive error handling:
- Input validation
- Duplicate ID prevention
- Email format validation
- Phone number validation
- Salary validation (must be positive)
- Department-based filtering
- File I/O error handling

## Future Enhancements

- Database integration (SQLite/MySQL)
- Web interface (Flask/Django)
- Role-based access control
- Performance reports
- Tax calculations
- Attendance tracking
- Leave management

## Author

Created as a demonstration of OOP principles in Python.

## License

Free to use and modify for educational purposes.
