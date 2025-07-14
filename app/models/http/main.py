from pydantic import BaseModel


class MainStatus(BaseModel):
    code: int
    error: bool
    message: str
    type: str


class MainErrorResponse(BaseModel):
    data: str
    status: MainStatus
