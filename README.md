# FastAPI Task Tracker

## Overview
A lightweight task management API with CRUD operations, built with FastAPI and in-memory storage.

## Quick Start
1. Clone repo: `git clone https://github.com/yourusername/task_tracker.git`
2. Enter directory: `cd task_tracker`
3. Create venv: `python -m venv .venv`
4. Activate:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
5. Install deps: `pip install -r requirements.txt`
6. Run: `uvicorn app.main:app --reload`

## API Endpoints
| Method | Endpoint       | Description          |
|--------|----------------|----------------------|
| GET    | /tasks         | List all tasks       |
| POST   | /tasks         | Create new task      |
| GET    | /tasks/{id}    | Get single task      |
| PUT    | /tasks/{id}    | Update task          |
| DELETE | /tasks/{id}    | Delete task          |

## Usage Examples
```bash
# Create task
curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"title":"Learn FastAPI"}'

# List tasks
curl "http://localhost:8000/tasks"
