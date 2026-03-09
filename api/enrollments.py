from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.core.responses import success_response
from app.database import get_db
from app.schemas.enrollment import EnrollmentCreate, EnrollmentResponse
from app.services.enrollment_service import EnrollmentService

router = APIRouter(prefix="/enrollments", tags=["enrollments"])


@router.post("/", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def create_enrollment(data: EnrollmentCreate, db: Session = Depends(get_db)):
    service = EnrollmentService(db)
    result = service.enroll(data)

    if not result["success"]:
        raise HTTPException(status_code=result["status"], detail=result["message"])

    return result["enrollment"]

