from redis import Redis

def get_redis(settings: Settings = Depends(Settings)):
    return Redis.from_url(settings.redis_url)

@app.get("/add")
async def add_numbers(
    a: float, 
    b: float,
    redis: Redis = Depends(get_redis)
):
    result = a + b
    redis.incr("add_operations")
    return {"result": result}
