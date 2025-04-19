#  Flask and Django Web Applications with Docker Compose

##  Project Overview

This project demonstrates the use of **Flask** and **Django** frameworks, each running in its own Docker container and managed using **Docker Compose**.

- **Flask App**: A simple web application with routing, forms, and error handling.
- **Django App**: A project integrated with a database and an admin panel.

---

##  Project Structure

project-root/ ├── flask_app/ │ ├── app.py │ ├── requirements.txt │ └── Dockerfile ├── django_app/ │ ├── myproject/ │ │ ├── manage.py │ │ ├── requirements.txt │ │ └── Dockerfile ├── docker-compose.yml └── README.md


---

##  How to Run

### Prerequisites

- Docker installed (and Docker Desktop running)
- Git installed

### Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/project-root.git
cd project-root
```

2. **Build and Run Containers**
```bash
   docker-compose up --build
```

3. **Access the Applications**

Flask application: http://localhost:5000

Django application: http://localhost:8000

Django admin panel: http://localhost:8000/admin

### Features
## Flask Application
Homepage with a "Hello, World!" message.

Form to accept the user's name and age.

Input validation and a greeting page displaying the submitted information.

## Django Application
A list of items from the database.

A form to add new items to the database.

Admin panel to manage the items.

## Technologies Used
Flask for the simple web application with routing and forms.

Django for the database-driven application and admin panel.

Docker for containerizing both applications.

Docker Compose for managing multi-container Docker applications.

