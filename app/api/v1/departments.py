import os
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from ...models.http.main import MainErrorResponse
from ...exceptions.departments import (
    Departments404Exception,
)


DEPARTMENT_CODES = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "2A",
    "2B",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "971",
    "972",
    "973",
    "974",
    "976",
]


router = APIRouter()


@router.get(
    "/flag-image/{department_code}",
    tags=["Departments' Flags"],
    description="Get the PNG image of the flag of the French department corresponding to the provided department code",
    # response_model=FileResponse,
    responses={
        404: {"model": MainErrorResponse},
    },
)
async def get_flag_image(department_code: str):
    if department_code not in DEPARTMENT_CODES:
        raise Departments404Exception("Invalid department code. Department not found.")

    print(os.getcwd())
    image_path = Path(f"./assets/department_flags/{department_code}.svg.png")

    if not image_path.is_file():
        raise Departments404Exception("Department flag mage not found on the server")

    return FileResponse(image_path)
