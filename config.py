import dotenv
from os import getenv

dotenv.load_dotenv()


class Settings:
    REDIS_HOST=getenv('REDIS_HOST')
    REDIS_PORT=getenv('REDIS_PORT')


settings = Settings()