import os

from dotenv import load_dotenv
from pydantic import BaseSettings

# load .env from project
load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    API_VERSION: str = os.getenv('API_VERSION')
    API_VERSION_PREFIX: str = os.getenv('API_VERSION_PREFIX')
    ENVIRONMENT: str = os.getenv('ENVIRONMENT')
    INTENT_MODEL_PATH: str = os.getenv('INTENT_MODEL_PATH')
    NER_MODEL_PATH: str = os.getenv('NER_MODEL_PATH')


# make instance
settings = Settings()
