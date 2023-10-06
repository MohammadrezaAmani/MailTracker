from fastapi import FastAPI
from tracker.router import content

app = FastAPI()
app.include_router(content.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.167.186", port=8000)
