# app/main.py
from fastapi import FastAPI
from gumigest_app.api.v1 import user

app = FastAPI()

app.include_router(user.router)
