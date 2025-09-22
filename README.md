**Overview**

A backend service for managing personal tasks with user authentication. Users can register, log in, and manage tasks (CRUD). JWT authentication ensures each user only accesses their own tasks.

**Features**

- JWT-based user authentication (register/login)

- CRUD operations for tasks

- SQLite database (no setup required)

- RESTful API design principles

- Modular Flask blueprint structure

**Tech Stack**

- Python, Flask

- Flask-JWT-Extended

- SQLAlchemy (SQLite DB)

**Installation**

git clone <repo-url>
cd task-manager-api
pip install -r requirements.txt
python src/app.py

## API Endpoints

POST    /api/auth/register    → Register new user (No Auth)
POST    /api/auth/login       → Login + get token (No Auth)
GET     /api/tasks            → Get all tasks (Auth Required)
POST    /api/tasks            → Create a task (Auth Required)
GET     /api/tasks/<id>       → Get task by ID (Auth Required)
PUT     /api/tasks/<id>       → Update a task (Auth Required)
DELETE  /api/tasks/<id>       → Delete a task (Auth Required)
