from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    workload = Column(Integer, nullable=False)

    enrollments = relationship("Enrollment", back_populates="course")
    users = relationship(
        "User",
        secondary="enrollments",
        back_populates="courses",
    )

