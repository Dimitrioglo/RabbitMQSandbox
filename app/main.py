from fastapi import FastAPI

from app.routers import cars

app = FastAPI()


app.include_router(cars.router)
