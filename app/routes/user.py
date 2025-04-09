from fastapi import APIRouter
from app.models.user_model import UserCreate
from app.database import get_db_connection
from app.utils.hash_util import hash_password

router = APIRouter()

@router.post("/users/")
def create_user(user: UserCreate):
    hashed_password = hash_password(user.password)
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id;",
                (user.username, user.email, hashed_password)
            )
            user_id = cur.fetchone()[0]
            conn.commit()
    return {"id": user_id, "username": user.username, "email": user.email}
