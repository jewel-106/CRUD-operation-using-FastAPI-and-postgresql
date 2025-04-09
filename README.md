```markdown
# FastAPI Project

This is a FastAPI application with authentication, task management, and a PostgreSQL database. It demonstrates how to build a RESTful API with FastAPI, integrate JWT authentication, and interact with a PostgreSQL database.

## Features

- **User Management**: Create users, login with JWT authentication.
- **Task Management**: Create, update, delete, and list tasks.
- **JWT Authentication**: Secure API endpoints with JWT-based authentication.
- **PostgreSQL Database**: Interact with a PostgreSQL database to store user and task data.

## Project Structure
```

FastApiApp/
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── config.py
│ ├── database.py
│ ├── models/
│ │ ├── **init**.py
│ │ ├── user_model.py
│ │ └── task_model.py
│ ├── routes/
│ │ ├── **init**.py
│ │ ├── auth.py
│ │ ├── user.py
│ │ └── task.py
│ └── utils/
│ ├── **init**.py
│ ├── jwt_util.py
│ └── hash_util.py
├── requirements.txt
└── .env

````

## Requirements

- Python 3.7+
- PostgreSQL
- `pip` for managing Python dependencies

## Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the repository

```bash
git clone <repository_url>
cd FastApiApp
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the environment variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```
DATABASE_URL=postgresql://<username>:<password>@localhost/<dbname>
SECRET_KEY=<your_secret_key>
ALGORITHM=HS256
```

Replace `<username>`, `<password>`, and `<dbname>` with your PostgreSQL credentials.

### 5. Run the application

To run the FastAPI app locally with auto-reloading, use `uvicorn`:

```bash
uvicorn app.main:app --reload
```

Your API will be running on `http://127.0.0.1:8000`.

### 6. Test the API

You can test the API by accessing the auto-generated documentation:

- Open your browser and go to `http://127.0.0.1:8000/docs` to access the Swagger UI.
- Alternatively, go to `http://127.0.0.1:8000/redoc` for ReDoc documentation.

## API Endpoints

### **Public Routes:**

- **POST /users/**: Create a new user.
- **POST /token**: Login and get a JWT token.

### **Protected Routes (Requires JWT Authentication):**

- **POST /tasks/**: Create a new task.
- **GET /tasks/**: List all tasks.
- **PUT /tasks/{task_id}**: Update a task.
- **DELETE /tasks/{task_id}**: Delete a task.

