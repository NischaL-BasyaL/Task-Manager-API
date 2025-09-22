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

**API Endpoints**
Method  	Endpoint	              Description	            Auth Required
POST	    /api/auth/register	    Register new user	      No
POST	    /api/auth/login	        Login + get token	      No
GET	        /api/tasks	            Get all user tasks	      Yes
POST	    /api/tasks	            Create a task	          Yes
PUT	        /api/tasks/<id>	        Update a task	          Yes
DELETE	    /api/tasks/<id>	        Delete a task	          Yes
