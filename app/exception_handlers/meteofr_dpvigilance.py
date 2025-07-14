from fastapi import status
from fastapi.responses import JSONResponse

from ..exceptions.meteofr_dpvigilance import (
    MeteoFrDPVigilance404Exception,
    MeteoFrDPVigilance500Exception,
)


async def meteofr_dp_vigilance_404_exc_handler(
    request, exc: MeteoFrDPVigilance404Exception
):
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


async def meteofr_dp_vigilance_500_exc_handler(
    request, exc: MeteoFrDPVigilance500Exception
):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "data": exc.message,
            "status": {
                "code": 500,
                "error": True,
                "message": exc.message,
                "type": "Internal Server Error",
            },
        },
    )
