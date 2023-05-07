import logging.config

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.logger import logger
from starlette.middleware.cors import CORSMiddleware
from pythonjsonlogger import jsonlogger
from starlette.responses import JSONResponse

from config import settings
from src.api.router import api_router

# setup loggers
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

# get root logger
s_logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.

# create fastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_VERSION_PREFIX}/openapi.json",   # root_path=f"{settings.PROXY_ROOT_PATH}",
    docs_url="/docs"
)

# set cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """
    THis function allows to send response to FE when invalid pydantic validation happened.
    :rtype: object
    """
    err = exc.errors()
    logger.error(err)
    error_string = ""
    for e in err:
        error_string = error_string + str(e["loc"][-1]) + " - " + str(e["msg"]) + "\n"

    return JSONResponse(
        content=jsonable_encoder(
            {
                "code": 400,
                "status": "BAD REQUEST",
                "data": {
                    "error": error_string
                }
            }
        ),
        status_code=400,
    )

# include api router outside with prefix
app.include_router(api_router, prefix=f"/api{settings.API_VERSION_PREFIX}")

# setup logger
# s_logger = logging.getLogger("uvicorn")
s_logger.setLevel(logging.DEBUG)  # ['critical', 'error', 'warning', 'info', 'debug', 'trace'.]
logger.setLevel(s_logger.level)
logger.handlers = s_logger.handlers

