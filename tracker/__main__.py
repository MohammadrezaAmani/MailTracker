from fastapi import FastAPI

from tracker.router import content

app = FastAPI()
app.include_router(content.router)
app.mount("/tracker/assets", content.router, name="assets")
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
