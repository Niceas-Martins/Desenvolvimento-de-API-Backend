from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str | None = None
    workload: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    workload: int | None = None


class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True

