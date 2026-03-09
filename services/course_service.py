from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.course import Course
from app.repositories.course_repository import CourseRepository
from app.schemas.course import CourseCreate, CourseUpdate


class CourseService:
    def __init__(self, db: Session):
        self.repo = CourseRepository(db)

    def list_courses(self) -> List[Course]:
        return self.repo.get_all()

    def create_course(self, data: CourseCreate) -> Course:
        return self.repo.create(data)

    def get_course(self, course_id: int) -> Optional[Course]:
        return self.repo.get_by_id(course_id)

    def update_course(self, course_id: int, data: CourseUpdate) -> Optional[Course]:
        course = self.repo.get_by_id(course_id)
        if not course:
            return None
        return self.repo.update(course, data)

    def delete_course(self, course_id: int) -> bool:
        course = self.repo.get_by_id(course_id)
        if not course:
            return False
        self.repo.delete(course)
        return True

