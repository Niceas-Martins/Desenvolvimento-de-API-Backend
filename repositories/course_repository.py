from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


class CourseRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Course]:
        return self.db.query(Course).all()

    def get_by_id(self, course_id: int) -> Optional[Course]:
        return self.db.query(Course).filter(Course.id == course_id).first()

    def create(self, data: CourseCreate) -> Course:
        course = Course(
            title=data.title,
            description=data.description,
            workload=data.workload,
        )
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def update(self, course: Course, data: CourseUpdate) -> Course:
        if data.title is not None:
            course.title = data.title
        if data.description is not None:
            course.description = data.description
        if data.workload is not None:
            course.workload = data.workload
        self.db.commit()
        self.db.refresh(course)
        return course

    def delete(self, course: Course) -> None:
        self.db.delete(course)
        self.db.commit()

