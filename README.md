# ✅ FastAPI Todo App with Frontend

A simple, full-stack Todo application built with **FastAPI** (Python backend), **SQLite** (database), and a lightweight **HTML/JavaScript frontend**.

---

## 🚀 Features

- Create, Read, Update, and Delete (CRUD) tasks
- RESTful API using FastAPI
- SQLite database integration with SQLModel
- Interactive frontend to manage tasks
- CORS support for frontend-backend communication

---

## 📦 Tech Stack

- **Backend:** FastAPI, SQLModel
- **Database:** SQLite
- **Frontend:** HTML, CSS, Vanilla JavaScript

---

## 📘 API Documentation

### 1. Create a Task
- **Endpoint:** `POST /tasks/`
- **Description:** Add a new task to the database.
- **Request Body:**

```json
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "completed": false
}
```

- **Response:**

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "completed": false
}
```

---

### 2. Get All Tasks

- **Endpoint:** `GET /tasks/`
- **Description:** Retrieve all tasks from the database.
- **Response:**

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Bread, Eggs",
    "completed": false
  }
]
```

---

### 3. Get Task by ID

- **Endpoint:** `GET /tasks/{task_id}`
- **Description:** Retrieve a specific task by ID.
- **Response:**

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "completed": false
}
```

---

### 4. Update a Task

- **Endpoint:** `PUT /tasks/{task_id}`
- **Description:** Update a task's title, description, and completion status.
- **Request Body:**

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs, Butter",
  "completed": true
}
```

---

### 5. Delete a Task

- **Endpoint:** `DELETE /tasks/{task_id}`
- **Description:** Deletes a task based on ID.
- **Response:**

```json
{
  "message": "Task deleted successfully"
}
```

---

## 🗃️ Database Details

- **Type:** SQLite  
- **Library:** SQLModel (built on SQLAlchemy and Pydantic)  
- A local database file `database.db` is automatically created when you run the app.

---

## 🛠️ How to Run the Server (Backend)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-todo-app.git
cd fastapi-todo-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# For Windows
env\Scripts\activate

# For Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI to test all endpoints.

---

## 💻 How to Run the Frontend (Optional)

1. Open `index.html` in your browser
2. Make sure the backend server is running at `http://127.0.0.1:8000`
3. Use the interface to add, update, and delete tasks

---

## 🧪 Testing the API with curl (Optional)

```bash
# Create a task
curl -X POST "http://127.0.0.1:8000/tasks/" -H "Content-Type: application/json" -d '{"title": "Learn FastAPI", "description": "Study from docs", "completed": false}'

# Get all tasks
curl http://127.0.0.1:8000/tasks/

# Update a task
curl -X PUT "http://127.0.0.1:8000/tasks/1" -H "Content-Type: application/json" -d '{"id":1,"title":"Updated","description":"Updated desc","completed":true}'

# Delete a task
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

---


