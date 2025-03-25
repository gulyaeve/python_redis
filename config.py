import dotenv
from os import getenv
from dataclasses import dataclass

dotenv.load_dotenv()


class Settings:
    REDIS_HOST=getenv('REDIS_HOST')
    REDIS_PORT=getenv('REDIS_PORT')


settings = Settings()


@dataclass
class Coordinates():
    name: str
    lat: float
    lon: float

    def __init__(self, name: str, lat: float, lon: float):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get(self):
        return self.lon, self.lat, self.name
    
    # def __str__(self):
    #     return f"{self.lon} {self.lat} {self.name}"


if __name__ == "__main__":
    moscow = Coordinates("City", 1, 2)
    print(moscow.get())
