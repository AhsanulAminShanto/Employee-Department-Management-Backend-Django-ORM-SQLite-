# Employee Management System (Django ORM)

A **Django-based backend system** for managing employees, departments, and achievements.  
This project uses Django ORM for database operations, user authentication, and supports full CRUD operations.

---

## Features

- **User Authentication**  
  - Register, login, and logout using email & password.
- **Employee Management**  
  - Create, read, update, and delete employees.
  - Assign employees to departments.
  - Associate achievements with employees (many-to-many relationship).
- **Department Management**  
  - Create and manage departments.
- **Achievement Management**  
  - Create achievements and link them to employees.
- **Professional UI** (optional frontend templates)  
  - Clean and modern login/signup pages with gradient backgrounds and responsive design.
- **Employee-Achievement Pivot Table**  
  - Tracks achievements for each employee along with achievement dates.
- **Django Admin Support**  
  - Manage employees, departments, and achievements via Django admin panel.

---

## Tech Stack

- **Backend:** Python, Django 5.2  
- **Database:** SQLite (default), can be replaced with PostgreSQL or MySQL  
- **Authentication:** Django built-in auth system  
- **ORM:** Django ORM  
- **Frontend (Optional):** HTML, CSS  

---


## Setup Instructions
# 1. Clone the repository
git clone <your-repo-url>
cd PythonProject

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Windows (PowerShell):
.\venv\Scripts\activate
# macOS / Linux:
# source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate

# 6. Create a superuser (optional)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver

# 8. Access the application in your browser
# Open: http://127.0.0.1:8000/
✅ With this, anyone can **just copy and paste** the whole block into their terminal to set up the project quickly. 
