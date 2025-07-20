from fastapi import status
from fastapi import APIRouter

from ...models.http.main import MainErrorResponse
from ...services.meteofr_dpvigilance import meteofr_dpvigilance_service

router = APIRouter()


@router.get(
    "/textes-vigilance-encours",
    tags=["Météo France Public Vigilance Data"],
    description="Get the Meteo France vigilance public data texts",
    responses={
        404: {"model": MainErrorResponse},
        500: {"model": MainErrorResponse},
    },
)
async def get_textes_vigilance_encours():
    return {
        "data": meteofr_dpvigilance_service.get_dpvigilance_texts(),
        "status": {
            "code": 200,
            "error": False,
            "message": "",
            "type": "OK",
        },
    }
