from typing import List
from .schemas import Task

task_db: List[Task] = []
current_id = 0

def get_task_db():
    return task_db

def get_next_id():
    global current_id
    current_id += 1
    return current_id