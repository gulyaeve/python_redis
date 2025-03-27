from redis import Redis
from config import settings, Coordinates

cache = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)

for city in cache.sscan_iter("cities"):
    # city = cache.sca
    print(city)

# cache.set("a", "b")
# cache.setex("b", 3600, "hello")
#
#
# moscow = Coordinates("Moscow", 37.617698, 55.755864)
# cache.geoadd("cities2", moscow.get())
#
# a = [1, 2, 3]
#
# petya = {"name": "user", "age": 99}

# cache.hdel("user:1002", "name", "age")
# cache.hset("user:1002", mapping=petya)

# for item in a:
# cache.lpush("from_py", *a)

# print(cache.get("a"))
# print(cache.lrange("from_py", 0, -1))
# print(cache.hget("user:1002", "age"))
# print(cache.hget("user:1002", "name"))
# print(cache.geopos("cities2", "Moscow"))
