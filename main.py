from fastapi import FastAPI, HTTPException
import memcache

servers = [
    '127.0.0.1:11211', 
    '127.0.0.1:11212', 
    '127.0.0.1:11213'
]
client = memcache.Client(servers)

app = FastAPI()

@app.put("/cache/{key}")
def put(key: str, value: str):
    client.set(key, value)
    return {"message": f"Key '{key}' set successfully"}

@app.get("/cache/{key}")
def get(key: str):
    retrieved_value = client.get(key)
    if retrieved_value:
        return {"key": key, "value": retrieved_value.decode('utf-8')}
    else:
        raise HTTPException(status_code=404, detail=f"Key '{key}' not found")

@app.delete("/cache/{key}")
def delete(key: str):
    client.delete(key)
    return {"message": f"Key '{key}' deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
