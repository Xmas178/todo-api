# TODO API

A simple and clean REST API for task management, built with FastAPI and SQLite.

## Features

- **Full CRUD Operations** - Create, Read, Update, Delete tasks
- **SQLite Database** - Persistent data storage
- **Auto Documentation** - Interactive API docs with Swagger UI
- **Fast & Modern** - Built on FastAPI framework
- **Lightweight** - No external dependencies beyond Python packages

## Requirements

- Python 3.8+
- pip (Python package manager)

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/Xmas178/todo-api.git
cd todo-api
```

**2. Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

**3. Install dependencies**
```bash
pip install fastapi uvicorn sqlalchemy
```

**4. Run the server**
```bash
uvicorn main:app --reload
```

Server will start at: **http://localhost:8000**

## API Documentation

### Automatic Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### Get All Tasks
```http
GET /tasks
```

**Response:**
```json
[
  {
    "id": 1,
    "task": "Learn FastAPI",
    "completed": false
  }
]
```

#### Create New Task
```http
POST /tasks?task=New task
```

**Response:**
```json
{
  "id": 2,
  "task": "New task",
  "completed": false
}
```

#### Update Task Status
```http
PUT /tasks/1?completed=true
```

**Response:**
```json
{
  "id": 1,
  "task": "Learn FastAPI",
  "completed": true
}
```

#### Delete Task
```http
DELETE /tasks/1
```

**Response:**
```json
{
  "message": "Task deleted"
}
```

## Project Structure

```
todo-api/
├── main.py          # API routes and endpoints
├── database.py      # Database configuration and models
├── todos.db         # SQLite database (auto-generated)
├── venv/            # Virtual environment
└── README.md        # This file
```

## Testing

### Thunder Client (VS Code)

1. Install Thunder Client extension
2. Create new request
3. Test endpoints using examples above

### cURL Examples

```bash
# Get all tasks
curl http://localhost:8000/tasks

# Create task
curl -X POST "http://localhost:8000/tasks?task=Test%20task"

# Update task
curl -X PUT "http://localhost:8000/tasks/1?completed=true"

# Delete task
curl -X DELETE "http://localhost:8000/tasks/1"
```

## Technologies

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL database ORM
- **SQLite** - Lightweight database
- **Uvicorn** - ASGI web server

## What I Learned

- REST API fundamentals and HTTP methods (GET, POST, PUT, DELETE)
- FastAPI framework usage and best practices
- Database integration with SQLAlchemy ORM
- API documentation and interactive testing tools
- Building clean and maintainable API structure

## Future Development Ideas

- Add user authentication (JWT)
- Implement Pydantic models for data validation
- PostgreSQL support for production
- Unit tests with pytest
- Docker containerization
- Frontend integration (React/Vue)

## Author

**Xmas178**  
November 2024  
Portfolio Project

## License

This project is open source and available for learning purposes.
