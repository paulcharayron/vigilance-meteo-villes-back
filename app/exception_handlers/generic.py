from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def generic_422_exc_handler(request, exc: RequestValidationError):
    data = " | ".join(
        [
            (
                f"{error["msg"]}: {error["type"]} [{" > " \
                .join([str(loc) for loc in error["loc"]])}]"
            )
            for error in exc.errors()
        ]
    )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "data": data,
            "status": {
                "code": 422,
                "error": True,
                "message": data,
                "type": "Unprocessable Entity",
            },
        },
    )
