from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.course import CourseResponse

router = APIRouter(prefix="/users", tags=["relations"])


@router.get("/{user_id}/courses", response_model=dict)
def get_user_courses(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

    courses: List[CourseResponse] = user.courses  # type: ignore

    return {
        "success": True,
        "message": "Cursos do usuário retornados com sucesso.",
        "data": {
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "created_at": user.created_at,
            },
            "courses": courses,
        },
    }

