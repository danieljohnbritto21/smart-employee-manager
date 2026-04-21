"""
Utility module demonstrating advanced OOP concepts and helper functions.
"""

from employee import Employee, FullTimeEmployee, PartTimeEmployee, ContractEmployee
from typing import List, Callable
from datetime import datetime


class EmployeeAnalyzer:
    """Advanced analytics for employees using functional programming."""
    
    @staticmethod
    def filter_employees(employees: List[Employee], 
                        condition: Callable[[Employee], bool]) -> List[Employee]:
        """
        Filter employees based on condition.
        
        Args:
            employees: List of employees
            condition: Function that returns True/False
        
        Returns:
            Filtered list of employees
        """
        return [emp for emp in employees if condition(emp)]
    
    @staticmethod
    def get_high_earners(employees: List[Employee], threshold: float = 60000) -> List[Employee]:
        """Get employees earning above threshold."""
        return EmployeeAnalyzer.filter_employees(
            employees,
            lambda emp: emp.salary > threshold
        )
    
    @staticmethod
    def get_employees_by_type(employees: List[Employee], emp_type: str) -> List[Employee]:
        """Get employees of specific type."""
        type_map = {
            'fulltime': FullTimeEmployee,
            'parttime': PartTimeEmployee,
            'contract': ContractEmployee
        }
        
        target_type = type_map.get(emp_type.lower())
        if not target_type:
            return []
        
        return EmployeeAnalyzer.filter_employees(
            employees,
            lambda emp: isinstance(emp, target_type)
        )
    
    @staticmethod
    def calculate_department_stats(employees: List[Employee], department: str) -> dict:
        """Calculate statistics for a department."""
        dept_employees = EmployeeAnalyzer.filter_employees(
            employees,
            lambda emp: emp.department.lower() == department.lower()
        )
        
        if not dept_employees:
            return {}
        
        salaries = [emp.salary for emp in dept_employees]
        bonuses = [emp.calculate_bonus() for emp in dept_employees]
        
        return {
            'department': department,
            'employee_count': len(dept_employees),
            'total_salary': sum(salaries),
            'average_salary': sum(salaries) / len(salaries),
            'min_salary': min(salaries),
            'max_salary': max(salaries),
            'total_bonus': sum(bonuses),
            'average_bonus': sum(bonuses) / len(bonuses) if bonuses else 0,
            'employees': dept_employees
        }
    
    @staticmethod
    def get_salary_range_report(employees: List[Employee]) -> dict:
        """Get salary distribution report."""
        if not employees:
            return {}
        
        active_employees = EmployeeAnalyzer.filter_employees(
            employees,
            lambda emp: emp.is_active
        )
        
        if not active_employees:
            return {}
        
        salaries = [emp.salary for emp in active_employees]
        salaries.sort()
        
        ranges = {
            'under_40k': 0,
            '40k_60k': 0,
            '60k_80k': 0,
            '80k_plus': 0
        }
        
        for salary in salaries:
            if salary < 40000:
                ranges['under_40k'] += 1
            elif salary < 60000:
                ranges['40k_60k'] += 1
            elif salary < 80000:
                ranges['60k_80k'] += 1
            else:
                ranges['80k_plus'] += 1
        
        return {
            'ranges': ranges,
            'min_salary': min(salaries),
            'max_salary': max(salaries),
            'median_salary': salaries[len(salaries) // 2],
            'average_salary': sum(salaries) / len(salaries)
        }
    
    @staticmethod
    def compare_employees(emp1: Employee, emp2: Employee) -> dict:
        """Compare two employees."""
        return {
            'emp1_name': emp1.name,
            'emp2_name': emp2.name,
            'salary_difference': emp1.salary - emp2.salary,
            'emp1_bonus': emp1.calculate_bonus(),
            'emp2_bonus': emp2.calculate_bonus(),
            'emp1_total_comp': emp1.salary + emp1.calculate_bonus(),
            'emp2_total_comp': emp2.salary + emp2.calculate_bonus(),
            'higher_earner': emp1.name if emp1.salary > emp2.salary else emp2.name,
            'salary_ratio': round(max(emp1.salary, emp2.salary) / min(emp1.salary, emp2.salary), 2)
        }


class EmployeeReportGenerator:
    """Generate various reports for employees."""
    
    @staticmethod
    def generate_summary_report(employees: List[Employee]) -> str:
        """Generate a summary report."""
        active = [e for e in employees if e.is_active]
        inactive = [e for e in employees if not e.is_active]
        
        fulltime = len(EmployeeAnalyzer.get_employees_by_type(active, 'fulltime'))
        parttime = len(EmployeeAnalyzer.get_employees_by_type(active, 'parttime'))
        contract = len(EmployeeAnalyzer.get_employees_by_type(active, 'contract'))
        
        total_salary = sum(e.salary for e in active)
        total_bonus = sum(e.calculate_bonus() for e in active)
        
        report = f"""
{'='*70}
EMPLOYEE MANAGEMENT SYSTEM - SUMMARY REPORT
{'='*70}

HEADCOUNT SUMMARY:
  • Total Employees: {len(employees)}
  • Active Employees: {len(active)}
  • Inactive Employees: {len(inactive)}

EMPLOYEE TYPE BREAKDOWN (Active):
  • Full-Time: {fulltime}
  • Part-Time: {parttime}
  • Contract: {contract}

FINANCIAL SUMMARY (Active):
  • Total Salary: ${total_salary:,.2f}
  • Total Bonus: ${total_bonus:,.2f}
  • Total Compensation: ${total_salary + total_bonus:,.2f}
  • Average Salary: ${total_salary / len(active):,.2f}
  • Average Bonus: ${total_bonus / len(active):,.2f}

GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*70}
"""
        return report
    
    @staticmethod
    def generate_department_report(employees: List[Employee]) -> str:
        """Generate department-wise report."""
        departments = set(e.department for e in employees)
        
        report = f"\n{'='*70}\nDEPARTMENT-WISE REPORT\n{'='*70}\n"
        
        for dept in sorted(departments):
            stats = EmployeeAnalyzer.calculate_department_stats(employees, dept)
            if stats:
                report += f"""
DEPARTMENT: {stats['department'].upper()}
  • Employee Count: {stats['employee_count']}
  • Total Salary: ${stats['total_salary']:,.2f}
  • Average Salary: ${stats['average_salary']:,.2f}
  • Min Salary: ${stats['min_salary']:,.2f}
  • Max Salary: ${stats['max_salary']:,.2f}
  • Total Bonus: ${stats['total_bonus']:,.2f}
"""
        
        report += f"\n{'='*70}\n"
        return report
    
    @staticmethod
    def generate_salary_analysis(employees: List[Employee]) -> str:
        """Generate salary analysis report."""
        report_data = EmployeeAnalyzer.get_salary_range_report(employees)
        
        if not report_data:
            return "No employee data available for analysis.\n"
        
        ranges = report_data['ranges']
        
        report = f"""
{'='*70}
SALARY ANALYSIS REPORT
{'='*70}

SALARY DISTRIBUTION:
  • Under $40,000: {ranges['under_40k']} employees
  • $40,000 - $60,000: {ranges['40k_60k']} employees
  • $60,000 - $80,000: {ranges['60k_80k']} employees
  • $80,000+: {ranges['80k_plus']} employees

SALARY STATISTICS:
  • Minimum Salary: ${report_data['min_salary']:,.2f}
  • Maximum Salary: ${report_data['max_salary']:,.2f}
  • Median Salary: ${report_data['median_salary']:,.2f}
  • Average Salary: ${report_data['average_salary']:,.2f}

{'='*70}
"""
        return report


class EmployeeValidator:
    """Validation utilities for employee data."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        return '@' in email and '.' in email.split('@')[1]
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number."""
        digits = ''.join(c for c in phone if c.isdigit())
        return len(digits) >= 10
    
    @staticmethod
    def validate_salary(salary: float) -> bool:
        """Validate salary."""
        return salary > 0
    
    @staticmethod
    def validate_employee_data(name: str, email: str, phone: str, 
                               salary: float) -> tuple[bool, str]:
        """
        Validate all employee data.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not name or not name.strip():
            return False, "Name cannot be empty"
        
        if not EmployeeValidator.validate_email(email):
            return False, "Invalid email format"
        
        if not EmployeeValidator.validate_phone(phone):
            return False, "Invalid phone number (must have at least 10 digits)"
        
        if not EmployeeValidator.validate_salary(salary):
            return False, "Salary must be positive"
        
        return True, "All data is valid"


# Example usage function
def demonstrate_utilities():
    """Demonstrate utility functions."""
    from employee_management import EmployeeManagementSystem
    
    ems = EmployeeManagementSystem()
    employees = ems.get_all_employees()
    
    if employees:
        print(EmployeeReportGenerator.generate_summary_report(employees))
        print(EmployeeReportGenerator.generate_department_report(employees))
        print(EmployeeReportGenerator.generate_salary_analysis(employees))


if __name__ == "__main__":
    demonstrate_utilities()
