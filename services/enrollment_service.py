from sqlalchemy.orm import Session

from app.models.user import User
from app.models.course import Course
from app.repositories.enrollment_repository import EnrollmentRepository
from app.schemas.enrollment import EnrollmentCreate


class EnrollmentService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = EnrollmentRepository(db)

    def enroll(self, data: EnrollmentCreate) -> dict:
        # Verifica duplicidade
        existing = self.repo.get_by_user_and_course(data.user_id, data.course_id)
        if existing:
            return {
                "success": False,
                "status": 409,
                "message": "Usuário já está matriculado neste curso.",
                "enrollment": existing,
            }

        # Verifica existência de usuário e curso usando o ORM
        user_exists = self.db.query(User).filter(User.id == data.user_id).first()
        if not user_exists:
            return {
                "success": False,
                "status": 404,
                "message": "Usuário não encontrado.",
                "enrollment": None,
            }

        course_exists = self.db.query(Course).filter(Course.id == data.course_id).first()
        if not course_exists:
            return {
                "success": False,
                "status": 404,
                "message": "Curso não encontrado.",
                "enrollment": None,
            }

        enrollment = self.repo.create(data)

        return {
            "success": True,
            "status": 201,
            "message": "Matrícula criada com sucesso.",
            "enrollment": enrollment,
        }

