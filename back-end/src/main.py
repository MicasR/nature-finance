from fastapi import FastAPI
from src.modules.auth.routes import router as auth_routes

app = FastAPI()
app.include_router(auth_routes)


@app.get("/")
async def root():
    return {"message": "Hello World"}
