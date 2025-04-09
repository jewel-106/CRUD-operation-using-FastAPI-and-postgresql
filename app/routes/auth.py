from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db_connection
from app.utils.hash_util import verify_password
from app.utils.jwt_util import create_token

router = APIRouter()

@router.post("/token")
def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, email, password FROM users WHERE username = %s;", (form_data.username,))
            user = cur.fetchone()

    if not user or not verify_password(form_data.password, user[3]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user[1]})  # username as subject
    return {"access_token": token, "token_type": "bearer"}
