# How to Run the Web Application

## Quick Start

### Step 1: Install Flask
```bash
pip install flask
```

### Step 2: Navigate to Project Directory
```bash
cd "Employee Management System"
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Open Browser
```
http://localhost:5000
```

---

## Detailed Instructions

### Windows
1. Open Command Prompt or PowerShell
2. Navigate to the project folder:
   ```
   cd D:\Employee Management System
   ```
3. Run Flask:
   ```
   python app.py
   ```
4. Open your browser and go to: `http://localhost:5000`

### Mac/Linux
1. Open Terminal
2. Navigate to the project folder:
   ```bash
   cd /path/to/Employee\ Management\ System
   ```
3. Run Flask:
   ```bash
   python3 app.py
   ```
4. Open your browser and go to: `http://localhost:5000`

---

## What You'll See

When the application starts, you'll see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

This means the server is running and ready to use!

---

## Main Pages

### Dashboard (Home)
```
http://localhost:5000/
```
- Overview of all statistics
- Quick action buttons

### All Employees
```
http://localhost:5000/employees
```
- Table of all employees
- View, edit, delete options

### Add Employee
```
http://localhost:5000/add-employee
```
- Form to add new employees
- Support for different employee types

### Search
```
http://localhost:5000/search
```
- Search employees by ID, name, or department

### Statistics
```
http://localhost:5000/statistics
```
- System-wide statistics and insights

---

## Employee Types

### Full-Time Employee
- Bonus: 10% of salary
- Additional field: Benefits (list)
- Example:
  - Name: John Doe
  - Salary: $50,000
  - Bonus: $5,000
  - Benefits: Health Insurance, 401K

### Part-Time Employee
- Bonus: 5% of salary
- Additional field: Hours per week
- Example:
  - Name: Jane Smith
  - Salary: $30,000
  - Bonus: $1,500
  - Hours: 25/week

### Contract Employee
- Bonus: 0% (no bonus)
- Additional field: Contract end date
- Example:
  - Name: Bob Wilson
  - Salary: $45,000
  - Bonus: $0
  - End Date: 2024-12-31

---

## Sample Data

To add sample employees, you can use these values:

**Full-Time:**
- ID: E001
- Name: Alice Johnson
- Email: alice@company.com
- Phone: (555) 123-4567
- Department: IT
- Salary: 75000
- Benefits: Health Insurance, 401K, Dental

**Part-Time:**
- ID: E002
- Name: Bob Smith
- Email: bob@company.com
- Phone: (555) 234-5678
- Department: HR
- Salary: 40000
- Hours: 25

**Contract:**
- ID: E003
- Name: Carol Davis
- Email: carol@company.com
- Phone: (555) 345-6789
- Department: Finance
- Salary: 50000
- End Date: 2024-12-31

---

## Common Issues

### Port 5000 Already in Use
If you get an error that port 5000 is already in use:

1. **Change the port** in `app.py`:
   ```python
   if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0', port=8000)
   ```
   Then visit: `http://localhost:8000`

2. **Or stop the other service** using port 5000

### Flask Not Found
```bash
pip install flask
```

### Python Not Found
Make sure Python is installed and added to PATH:
```bash
python --version
# or
python3 --version
```

### ModuleNotFoundError
Make sure you're in the correct directory:
```bash
cd "Employee Management System"
```

---

## Features Available

✅ Add new employees  
✅ View all employees  
✅ Edit employee information  
✅ Delete employees  
✅ Search by ID, name, or department  
✅ View employee details  
✅ Manage active/inactive status  
✅ View statistics  
✅ JSON API endpoint  
✅ Responsive design  
✅ Data persistence  

---

## Keyboard Shortcuts

While browsing:
- `Ctrl/Cmd + D` - Bookmark page
- `Ctrl/Cmd + R` - Refresh page
- `Ctrl/Cmd + F` - Search on page

---

## Stopping the Application

### Windows/Mac/Linux
Press `Ctrl + C` in the terminal

---

## File Organization

```
Employee Management System/
├── app.py                    ← Flask application (RUN THIS)
├── employee.py              ← Employee classes
├── employee_management.py   ← Core system
├── templates/               ← HTML files
│   ├── base.html           ← Main template with styling
│   ├── index.html          ← Dashboard
│   ├── employees.html      ← Employee list
│   ├── add_employee.html   ← Add form
│   ├── view_employee.html  ← Details page
│   ├── search.html         ← Search page
│   └── ...
├── employees.json          ← Data file (auto-created)
└── WEB_README.md           ← Web documentation
```

---

## Next Steps

1. **Run the application** - `python app.py`
2. **Add sample employees** - Use the "Add Employee" form
3. **Explore features** - Click through the navigation
4. **Customize** - Edit colors and styling in templates

---

## Need Help?

- Check the **WEB_README.md** for detailed documentation
- Review the **OOP_CONCEPTS.md** for backend structure
- Check browser console for JavaScript errors (F12)
- Look at **app.py** for route definitions

---

**Enjoy using the Employee Management System!** 🎉

Access the web app at: **http://localhost:5000**
