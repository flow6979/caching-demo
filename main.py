from fastapi import FastAPI, HTTPException
from pymemcache.client.base import Client

app = FastAPI()

def get_memcached_clients():
    return [
        Client(('localhost', 11211)),
        Client(('localhost', 11212)),
        Client(('localhost', 11213))
    ]

@app.get("/get/{key}")
async def get_value(key: str):
    clients = get_memcached_clients()
    client = clients[hash(key) % len(clients)]
    value = client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "value": value.decode("utf-8")}

@app.put("/put/{key}")
async def put_value(key: str, value: str):
    clients = get_memcached_clients()
    client = clients[hash(key) % len(clients)]
    client.set(key, value.encode("utf-8"))
    return {"key": key, "value": value}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

