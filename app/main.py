from fastapi import FastAPI
from app.config.app_config import getAppConfig
from app.routers import auth

config = getAppConfig()

app = FastAPI(title=config.app_name)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": f"Welcome to {config.app_name}"}