"""Flask web application for the Employee Management System."""

from datetime import datetime

from flask import Flask, flash, jsonify, redirect, render_template, request, url_for

from employee_management import EmployeeManagementSystem

app = Flask(__name__)
app.secret_key = "employee-management-secret"

ems = EmployeeManagementSystem()


def format_currency(value):
    """Format a number for display."""
    return f"{value:,.2f}"


def build_stats():
    """Build dashboard and statistics data."""
    employees = ems.get_all_employees()
    active_employees = ems.get_active_employees()
    total_salary = ems.calculate_total_salary()
    total_bonus = ems.calculate_total_bonus()

    return {
        "total_employees": len(employees),
        "active_employees": len(active_employees),
        "inactive_employees": len(employees) - len(active_employees),
        "total_salary": format_currency(total_salary),
        "total_bonus": format_currency(total_bonus),
        "total_compensation": format_currency(total_salary + total_bonus),
        "average_salary": format_currency(total_salary / len(active_employees)) if active_employees else "0.00",
    }


def serialize_employee(employee):
    """Convert an employee object into template-friendly data."""
    bonus = employee.calculate_bonus()
    return {
        "emp_id": employee.emp_id,
        "name": employee.name,
        "department": employee.department,
        "salary": format_currency(employee.salary),
        "email": employee.email,
        "phone": employee.phone,
        "job_title": employee.get_job_title(),
        "bonus": format_currency(bonus),
        "joining_date": employee.joining_date,
        "status": "Active" if employee.is_active else "Inactive",
        "is_active": employee.is_active,
        "type": type(employee).__name__,
        "total_compensation": format_currency(employee.salary + bonus),
        "benefits": ", ".join(employee.benefits) if hasattr(employee, "benefits") and employee.benefits else "",
        "hours_per_week": getattr(employee, "hours_per_week", ""),
        "contract_end_date": getattr(employee, "contract_end_date", ""),
    }


@app.context_processor
def inject_globals():
    """Inject common values into templates."""
    return {"current_year": datetime.now().year}


@app.route("/")
def index():
    """Home page dashboard."""
    employees = ems.get_all_employees()
    recent_employees = [serialize_employee(employee) for employee in employees[-3:]][::-1]
    return render_template("index.html", stats=build_stats(), recent_employees=recent_employees)


@app.route("/employees")
def employees():
    """Display all employees."""
    employees_data = [serialize_employee(employee) for employee in ems.get_all_employees()]
    return render_template("employees.html", employees=employees_data)


@app.route("/add-employee", methods=["GET", "POST"])
def add_employee():
    """Add a new employee."""
    if request.method == "POST":
        try:
            emp_id = request.form.get("emp_id", "").strip()
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            phone = request.form.get("phone", "").strip()
            department = request.form.get("department", "").strip()
            salary = float(request.form.get("salary", 0))
            joining_date = request.form.get("joining_date", "").strip()
            emp_type = request.form.get("emp_type", "").strip()

            if not emp_id or not name or not email or not phone or not department or not joining_date or not emp_type:
                flash("Please fill in all required fields.", "error")
                return render_template("add_employee.html")

            if ems.get_employee(emp_id):
                flash(f"Employee ID {emp_id} already exists. Use a different ID.", "error")
                return render_template("add_employee.html")

            if "@" not in email:
                flash("Please enter a valid email address.", "error")
                return render_template("add_employee.html")

            if len(phone) < 10:
                flash("Phone number must be at least 10 digits/characters.", "error")
                return render_template("add_employee.html")

            if salary <= 0:
                flash("Salary must be greater than 0.", "error")
                return render_template("add_employee.html")

            if emp_type == "fulltime":
                benefits = [item.strip() for item in request.form.get("benefits", "").split(",") if item.strip()]
                success = ems.add_employee(
                    "fulltime",
                    emp_id,
                    name,
                    email,
                    phone,
                    department,
                    salary,
                    joining_date,
                    benefits=benefits,
                )
            elif emp_type == "parttime":
                hours_per_week = request.form.get("hours_per_week", "").strip() or "20"
                success = ems.add_employee(
                    "parttime",
                    emp_id,
                    name,
                    email,
                    phone,
                    department,
                    salary,
                    joining_date,
                    hours_per_week=float(hours_per_week),
                )
            elif emp_type == "contract":
                contract_end_date = request.form.get("contract_end_date", "").strip()
                if not contract_end_date:
                    flash("Please select a contract end date for contract employees.", "error")
                    return render_template("add_employee.html")
                success = ems.add_employee(
                    "contract",
                    emp_id,
                    name,
                    email,
                    phone,
                    department,
                    salary,
                    joining_date,
                    contract_end_date=contract_end_date,
                )
            else:
                flash("Please choose a valid employee type.", "error")
                return render_template("add_employee.html")

            if success:
                flash(f"Employee {name} added successfully.", "success")
                return redirect(url_for("employees"))

            flash("Unable to add employee. Please review the entered values.", "error")
        except Exception as exc:
            flash(f"Error: {exc}", "error")

    return render_template("add_employee.html")


@app.route("/edit-employee/<emp_id>", methods=["GET", "POST"])
def edit_employee(emp_id):
    """Edit employee information."""
    employee = ems.get_employee(emp_id)
    if not employee:
        flash("Employee not found.", "error")
        return redirect(url_for("employees"))

    if request.method == "POST":
        try:
            updates = {
                "name": request.form.get("name", "").strip(),
                "email": request.form.get("email", "").strip(),
                "phone": request.form.get("phone", "").strip(),
                "department": request.form.get("department", "").strip(),
                "salary": float(request.form.get("salary", 0)),
            }
            ems.update_employee(emp_id, **updates)
            flash("Employee updated successfully.", "success")
            return redirect(url_for("view_employee", emp_id=emp_id))
        except Exception as exc:
            flash(f"Error: {exc}", "error")

    return render_template("edit_employee.html", employee=serialize_employee(employee))


@app.route("/employee/<emp_id>")
def view_employee(emp_id):
    """View employee details."""
    employee = ems.get_employee(emp_id)
    if not employee:
        flash("Employee not found.", "error")
        return redirect(url_for("employees"))

    return render_template("view_employee.html", employee=serialize_employee(employee))


@app.route("/delete-employee/<emp_id>", methods=["POST"])
def delete_employee(emp_id):
    """Delete an employee."""
    try:
        ems.delete_employee(emp_id)
        flash("Employee deleted successfully.", "success")
    except Exception as exc:
        flash(f"Error: {exc}", "error")
    return redirect(url_for("employees"))


@app.route("/search", methods=["GET", "POST"])
def search():
    """Search employees by ID, name, or department."""
    search_term = request.values.get("search_term", "").strip()
    results = [serialize_employee(employee) for employee in ems.search_employee(search_term)] if search_term else []
    return render_template("search.html", results=results, search_term=search_term)


@app.route("/department/<dept_name>")
def view_department(dept_name):
    """View employees in a department."""
    employees_data = [serialize_employee(employee) for employee in ems.get_employees_by_department(dept_name)]
    return render_template("department.html", department=dept_name, employees=employees_data)


@app.route("/deactivate/<emp_id>", methods=["POST"])
def deactivate_employee(emp_id):
    """Deactivate an employee."""
    try:
        ems.deactivate_employee(emp_id)
        flash("Employee deactivated successfully.", "success")
    except Exception as exc:
        flash(f"Error: {exc}", "error")
    return redirect(url_for("view_employee", emp_id=emp_id))


@app.route("/activate/<emp_id>", methods=["POST"])
def activate_employee(emp_id):
    """Activate an employee."""
    try:
        ems.activate_employee(emp_id)
        flash("Employee activated successfully.", "success")
    except Exception as exc:
        flash(f"Error: {exc}", "error")
    return redirect(url_for("view_employee", emp_id=emp_id))


@app.route("/statistics")
def statistics():
    """Display system statistics."""
    return render_template("statistics.html", stats=build_stats())


@app.route("/api/employees")
def api_employees():
    """Return employees as JSON."""
    data = [serialize_employee(employee) for employee in ems.get_all_employees()]
    return jsonify(data)


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
