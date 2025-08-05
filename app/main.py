from fastapi import FastAPI, HTTPException, Depends, status
from .schemas import TaskCreate, Task
from .deps import get_task_db, get_next_id

app = FastAPI()

@app.get("/tasks", response_model=list[Task])
def read_tasks(completed: bool = None, db: list = Depends(get_task_db)):
    if completed is None:
        return db
    return [task for task in db if task.completed == completed]

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: list = Depends(get_task_db)):
    for task in db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: list = Depends(get_task_db)):
    new_task = Task(
        id=get_next_id(),
        title=task.title,
        description=task.description,
        completed=False
    )
    db.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskCreate, db: list = Depends(get_task_db)):
    for index, task in enumerate(db):
        if task.id == task_id:
            updated_task = Task(
                id=task_id,
                title=task_update.title,
                description=task_update.description,
                completed=db[index].completed  # Preserve existing completion status
            )
            db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: list = Depends(get_task_db)):
    for index, task in enumerate(db):
        if task.id == task_id:
            db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")