from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from .core.config import settings
from .api.v1 import (
    departments as departments_router,
    meteofr_dpvigilance as meteofr_dpvigilance_router,
)
from .exceptions.departments import (
    Departments404Exception,
)
from .exceptions.meteofr_dpvigilance import (
    MeteoFrDPVigilance404Exception,
    MeteoFrDPVigilance500Exception,
)
from .exception_handlers.generic import (
    generic_422_exc_handler,
)
from .exception_handlers.departments import (
    departments_404_exc_handler,
)
from .exception_handlers.meteofr_dpvigilance import (
    meteofr_dp_vigilance_404_exc_handler,
    meteofr_dp_vigilance_500_exc_handler,
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(RequestValidationError, generic_422_exc_handler)
app.add_exception_handler(Departments404Exception, departments_404_exc_handler)
app.add_exception_handler(
    MeteoFrDPVigilance404Exception, meteofr_dp_vigilance_404_exc_handler
)
app.add_exception_handler(
    MeteoFrDPVigilance500Exception, meteofr_dp_vigilance_500_exc_handler
)

app.include_router(
    departments_router.router,
    prefix="/api/v1/departments",
)
app.include_router(
    meteofr_dpvigilance_router.router,
    prefix="/api/v1/meteofr/dpvigilance",
)
