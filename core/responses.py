from fastapi import status
from fastapi.responses import JSONResponse


def success_response(data=None, message: str | None = None, status_code: int = status.HTTP_200_OK) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data,
        },
    )


def error_response(message: str, status_code: int = status.HTTP_400_BAD_REQUEST, data=None) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "data": data,
        },
    )

