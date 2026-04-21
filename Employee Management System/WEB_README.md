# Employee Management System - Web Version

A modern web-based Employee Management System built with Flask and HTML/CSS. This provides a user-friendly interface for managing employee records.

## Features

### Dashboard
- Quick overview of system statistics
- Total employees, active/inactive counts
- Total salary and bonus calculations
- Quick action buttons

### Employee Management
- ✅ **View All Employees** - Display all employees in a table format
- ✅ **Add Employee** - Add new employees (Full-Time, Part-Time, Contract)
- ✅ **View Employee Details** - See complete employee information
- ✅ **Edit Employee** - Update employee information
- ✅ **Delete Employee** - Remove employee records
- ✅ **Search Employees** - Search by ID, name, or department
- ✅ **View by Department** - Filter employees by department
- ✅ **Deactivate/Activate** - Manage employee status

### Statistics
- System-wide statistics and insights
- Financial calculations
- Employee headcount breakdown

## Installation

### Prerequisites
- Python 3.7+
- Flask (already installed)

### Setup

1. **Install Flask** (if not already installed):
```bash
pip install flask
```

2. **Navigate to project directory**:
```bash
cd "Employee Management System"
```

3. **Run the application**:
```bash
python app.py
```

4. **Open in browser**:
```
http://localhost:5000
```

## Usage

### Dashboard
- Main page shows key metrics
- Quick access to main features
- Statistics at a glance

### Adding an Employee
1. Click "Add Employee" or go to `/add-employee`
2. Select employee type (Full-Time, Part-Time, Contract)
3. Enter employee details
4. Add type-specific information:
   - **Full-Time**: Benefits
   - **Part-Time**: Hours per week
   - **Contract**: Contract end date
5. Click "Add Employee"

### Viewing Employees
1. Click "Employees" to view all employees
2. Table displays all employee information
3. Quick action buttons (View, Edit, Delete)

### Searching
1. Go to "Search" page
2. Enter search term (ID, name, or department)
3. View matching results

### Employee Details
- Click "View" on any employee
- See complete information
- Edit, deactivate, or delete
- View calculated salary and bonus

## Project Structure

```
Employee Management System/
├── app.py                      # Flask application
├── templates/
│   ├── base.html              # Base template with styling
│   ├── index.html             # Dashboard
│   ├── employees.html         # Employee list
│   ├── add_employee.html      # Add employee form
│   ├── edit_employee.html     # Edit employee form
│   ├── view_employee.html     # Employee details
│   ├── search.html            # Search page
│   ├── department.html        # Department view
│   ├── statistics.html        # Statistics page
│   ├── 404.html               # 404 error page
│   └── 500.html               # 500 error page
├── employee.py                # Employee classes
├── employee_management.py     # Management system
└── employees.json             # Data file
```

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Dashboard |
| `/employees` | GET | All employees |
| `/add-employee` | GET, POST | Add new employee |
| `/employee/<id>` | GET | View employee details |
| `/edit-employee/<id>` | GET, POST | Edit employee |
| `/delete-employee/<id>` | POST | Delete employee |
| `/search` | GET, POST | Search employees |
| `/department/<name>` | GET | View department employees |
| `/deactivate/<id>` | POST | Deactivate employee |
| `/activate/<id>` | POST | Activate employee |
| `/statistics` | GET | System statistics |
| `/api/employees` | GET | JSON API endpoint |

## Features

### Responsive Design
- Works on desktop, tablet, and mobile
- Modern and clean UI
- Intuitive navigation

### Data Persistence
- All data saved to `employees.json`
- Automatic backup on each operation
- Load existing data on startup

### Error Handling
- Input validation
- User-friendly error messages
- 404 and 500 error pages

### Styling
- Modern gradient design
- Color-coded cards and badges
- Smooth transitions and animations
- Professional appearance

## Customization

### Changing Port
Edit `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # Change 5000 to desired port
```

### Changing Colors
Edit `templates/base.html` CSS variables:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --success-color: #27ae60;
    /* ... more colors */
}
```

### Adding New Pages
1. Create new HTML template in `templates/`
2. Extend `base.html`
3. Add route in `app.py`

## API Endpoints

### Get All Employees (JSON)
```
GET /api/employees
```

Returns JSON array of all employees.

## Tips

1. **Search Tips**:
   - Search by Employee ID (e.g., "E001")
   - Search by Name (partial match works)
   - Search by Department

2. **Employee Types**:
   - **Full-Time**: 10% bonus, benefits
   - **Part-Time**: 5% bonus, hours/week
   - **Contract**: No bonus, end date

3. **Backup**:
   - Regularly backup `employees.json`
   - Export as JSON from `/api/employees` endpoint

## Troubleshooting

### Flask not found
```bash
pip install flask
```

### Port already in use
Change the port in `app.py` or stop the service using the port.

### Data not persisting
Check if `employees.json` exists and has write permissions.

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- User authentication
- Role-based access control
- Advanced filtering and sorting
- Export to CSV/PDF
- Charts and graphs
- Email notifications
- API documentation (Swagger)

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Data**: JSON file storage
- **OOP**: Python classes and inheritance

## License

Free to use and modify for educational purposes.

---

**Happy Employee Management!** 🎉
