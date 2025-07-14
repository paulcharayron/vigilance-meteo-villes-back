from fastapi import status
from fastapi.responses import JSONResponse

from ..exceptions.departments import (
    Departments404Exception,
)


async def departments_404_exc_handler(request, exc: Departments404Exception):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "data": exc.message,
            "status": {
                "code": 404,
                "error": True,
                "message": exc.message,
                "type": "Not Found",
            },
        },
    )
