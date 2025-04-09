from fastapi import APIRouter, Depends
from app.models.task_model import TaskCreate
from app.database import get_db_connection
from app.utils.jwt_util import get_current_user

router = APIRouter()

@router.post("/tasks/")
def create_task(task: TaskCreate, username: str = Depends(get_current_user)):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO tasks (title, description, user_id) VALUES (%s, %s, %s) RETURNING id;",
                (task.title, task.description, task.user_id)
            )
            task_id = cur.fetchone()[0]
            conn.commit()
    return {"id": task_id, "title": task.title, "description": task.description, "user_id": task.user_id}

@router.get("/tasks/")
def list_tasks(username: str = Depends(get_current_user)):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT tasks.id, tasks.title, tasks.description, users.username, users.email
                FROM tasks
                JOIN users ON tasks.user_id = users.id;
            """)
            tasks = cur.fetchall()

    return [{"id": t[0], "title": t[1], "description": t[2], "username": t[3], "email": t[4]} for t in tasks]

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, username: str = Depends(get_current_user)):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE tasks SET title = %s, description = %s WHERE id = %s;", (task.title, task.description, task_id))
            conn.commit()
    return {"id": task_id, "title": task.title, "description": task.description}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, username: str = Depends(get_current_user)):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
            conn.commit()
    return {"message": f"Task with id {task_id} has been deleted."}
