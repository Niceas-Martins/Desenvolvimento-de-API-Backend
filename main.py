from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from app.api import users, courses, enrollments, relations
from app.core.responses import error_response
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="StudyManager API - FastAPI")


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    # Tratamento genérico para erros de integridade, como duplicidade de chave única
    return error_response("Violação de integridade dos dados.", status_code=400)


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # Fallback para erros não tratados
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Erro interno no servidor.",
            "data": None,
        },
    )


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(enrollments.router)
app.include_router(relations.router)

