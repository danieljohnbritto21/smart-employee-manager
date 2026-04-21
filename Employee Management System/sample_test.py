"""
Sample script demonstrating Employee Management System usage.
Shows how to use the system programmatically.
"""

from employee_management import EmployeeManagementSystem
from datetime import datetime


def main():
    """Demonstrate the Employee Management System."""
    
    print("="*70)
    print("EMPLOYEE MANAGEMENT SYSTEM - SAMPLE DEMONSTRATION")
    print("="*70)
    
    # Initialize the system
    ems = EmployeeManagementSystem()
    
    # ========== ADD EMPLOYEES ==========
    print("\n[1] Adding Sample Employees...")
    print("-"*70)
    
    # Add Full-Time Employees
    ems.add_employee(
        'fulltime',
        emp_id='E001',
        name='Alice Johnson',
        email='alice.johnson@company.com',
        phone='(555) 123-4567',
        department='IT',
        salary=75000,
        joining_date='2021-03-15',
        benefits=['Health Insurance', 'Dental Coverage', '401K', 'Stock Options']
    )
    
    ems.add_employee(
        'fulltime',
        emp_id='E002',
        name='Bob Smith',
        email='bob.smith@company.com',
        phone='(555) 234-5678',
        department='Finance',
        salary=65000,
        joining_date='2020-06-20',
        benefits=['Health Insurance', '401K', 'Tuition Reimbursement']
    )
    
    ems.add_employee(
        'fulltime',
        emp_id='E003',
        name='Carol Davis',
        email='carol.davis@company.com',
        phone='(555) 345-6789',
        department='HR',
        salary=60000,
        joining_date='2022-01-10',
        benefits=['Health Insurance', 'Flexible Hours', 'Remote Work']
    )
    
    # Add Part-Time Employees
    ems.add_employee(
        'parttime',
        emp_id='E004',
        name='David Wilson',
        email='david.wilson@company.com',
        phone='(555) 456-7890',
        department='IT',
        salary=40000,
        joining_date='2023-02-15',
        hours_per_week=25
    )
    
    ems.add_employee(
        'parttime',
        emp_id='E005',
        name='Emily Brown',
        email='emily.brown@company.com',
        phone='(555) 567-8901',
        department='Marketing',
        salary=35000,
        joining_date='2023-05-20',
        hours_per_week=20
    )
    
    # Add Contract Employee
    ems.add_employee(
        'contract',
        emp_id='E006',
        name='Frank Miller',
        email='frank.miller@company.com',
        phone='(555) 678-9012',
        department='Finance',
        salary=50000,
        joining_date='2023-09-01',
        contract_end_date='2024-08-31'
    )
    
    # ========== VIEW ALL EMPLOYEES ==========
    print("\n[2] All Employees in System:")
    print("-"*70)
    employees = ems.get_all_employees()
    for idx, emp in enumerate(employees, 1):
        print(f"{idx}. {emp}")
    
    # ========== SEARCH EMPLOYEES ==========
    print("\n[3] Search Examples:")
    print("-"*70)
    
    print("\n📍 Searching for employees in 'IT' department:")
    it_employees = ems.search_employee('IT')
    for emp in it_employees:
        print(f"  • {emp.name} - {emp.get_job_title()}")
    
    print("\n📍 Searching for employee 'Bob':")
    search_results = ems.search_employee('Bob')
    for emp in search_results:
        print(f"  • {emp.name} ({emp.emp_id}) - {emp.department}")
    
    # ========== DEPARTMENT VIEW ==========
    print("\n[4] Employees by Department:")
    print("-"*70)
    
    departments = {'IT', 'Finance', 'HR', 'Marketing'}
    for dept in departments:
        dept_employees = ems.get_employees_by_department(dept)
        print(f"\n{dept} Department ({len(dept_employees)} employees):")
        for emp in dept_employees:
            print(f"  • {emp.name} - ${emp.salary:,.2f}")
    
    # ========== EMPLOYEE DETAILS ==========
    print("\n[5] Detailed Employee Information:")
    print("-"*70)
    
    emp = ems.get_employee('E001')
    if emp:
        details = emp.get_details()
        print(f"\nEmployee Details for {emp.name}:")
        for key, value in details.items():
            if key not in ['emp_id', 'name']:
                print(f"  • {key.replace('_', ' ').title()}: {value}")
    
    emp_pt = ems.get_employee('E004')
    if emp_pt:
        details = emp_pt.get_details()
        print(f"\nEmployee Details for {emp_pt.name}:")
        for key, value in details.items():
            if key not in ['emp_id', 'name']:
                print(f"  • {key.replace('_', ' ').title()}: {value}")
    
    # ========== UPDATE EMPLOYEE ==========
    print("\n[6] Updating Employee Information:")
    print("-"*70)
    print(f"\nBefore update: {ems.get_employee('E002')}")
    ems.update_employee('E002', phone='(555) 999-9999', salary=70000)
    print(f"After update: {ems.get_employee('E002')}")
    
    # ========== DEACTIVATE EMPLOYEE ==========
    print("\n[7] Deactivating Employee:")
    print("-"*70)
    ems.deactivate_employee('E005')
    emp = ems.get_employee('E005')
    print(f"Employee {emp.name} status: {'Active' if emp.is_active else 'Inactive'}")
    
    # ========== ACTIVE/INACTIVE EMPLOYEES ==========
    print("\n[8] Active vs Inactive Employees:")
    print("-"*70)
    
    active = ems.get_active_employees()
    inactive = ems.get_inactive_employees()
    
    print(f"\nActive Employees ({len(active)}):")
    for emp in active:
        print(f"  • {emp.name} - {emp.department}")
    
    print(f"\nInactive Employees ({len(inactive)}):")
    for emp in inactive:
        print(f"  • {emp.name} - {emp.department}")
    
    # ========== CALCULATIONS ==========
    print("\n[9] Financial Calculations:")
    print("-"*70)
    
    total_salary = ems.calculate_total_salary()
    total_bonus = ems.calculate_total_bonus()
    avg_salary = total_salary / len(active) if active else 0
    
    print(f"\nTotal Active Employees: {len(active)}")
    print(f"Total Salary (Active): ${total_salary:,.2f}")
    print(f"Average Salary: ${avg_salary:,.2f}")
    print(f"Total Bonus: ${total_bonus:,.2f}")
    print(f"Total Compensation: ${total_salary + total_bonus:,.2f}")
    
    # ========== BONUS BREAKDOWN BY TYPE ==========
    print("\n[10] Bonus Breakdown by Employee Type:")
    print("-"*70)
    
    bonus_by_type = {}
    for emp in active:
        emp_type = type(emp).__name__
        if emp_type not in bonus_by_type:
            bonus_by_type[emp_type] = {'count': 0, 'total_bonus': 0}
        bonus_by_type[emp_type]['count'] += 1
        bonus_by_type[emp_type]['total_bonus'] += emp.calculate_bonus()
    
    for emp_type, data in bonus_by_type.items():
        avg_bonus = data['total_bonus'] / data['count'] if data['count'] > 0 else 0
        print(f"\n{emp_type}:")
        print(f"  • Count: {data['count']}")
        print(f"  • Total Bonus: ${data['total_bonus']:,.2f}")
        print(f"  • Average Bonus: ${avg_bonus:,.2f}")
    
    # ========== STATISTICS ==========
    print("\n[11] System Statistics:")
    print("-"*70)
    ems.display_statistics()
    
    # ========== REACTIVATE EMPLOYEE ==========
    print("[12] Reactivating Employee:")
    print("-"*70)
    ems.activate_employee('E005')
    emp = ems.get_employee('E005')
    print(f"Employee {emp.name} status: {'Active' if emp.is_active else 'Inactive'}")
    
    print("\n" + "="*70)
    print("Sample demonstration completed!")
    print("All data has been saved to 'employees.json'")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
