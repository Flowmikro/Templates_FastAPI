# Запускаем
from fastapi import FastAPI

from app.router import router_template

app = FastAPI()

app.include_router(router_template, prefix='/template')
