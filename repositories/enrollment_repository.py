from sqlalchemy.orm import Session
from typing import Optional, List

from app.models.enrollment import Enrollment
from app.schemas.enrollment import EnrollmentCreate


class EnrollmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_user_and_course(self, user_id: int, course_id: int) -> Optional[Enrollment]:
        return (
            self.db.query(Enrollment)
            .filter(Enrollment.user_id == user_id, Enrollment.course_id == course_id)
            .first()
        )

    def create(self, data: EnrollmentCreate) -> Enrollment:
        enrollment = Enrollment(
            user_id=data.user_id,
            course_id=data.course_id,
        )
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)
        return enrollment

    def get_by_user(self, user_id: int) -> List[Enrollment]:
        return self.db.query(Enrollment).filter(Enrollment.user_id == user_id).all()

