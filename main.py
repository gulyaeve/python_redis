from redis import Redis
from config import settings

cache = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)

cache.set("a", "b")
cache.setex("b", 3600, "hello")

a = [1, 2, 3]

petya = {"name": "user", "age": 99}

# cache.hdel("user:1002", "name", "age")
cache.hset("user:1002", mapping=petya)

# for item in a:
cache.lpush("from_py", *a)

print(cache.get("a"))
print(cache.lrange("from_py", 0, -1))
print(cache.hget("user:1002", "age"))
print(cache.hget("user:1002", "name"))
