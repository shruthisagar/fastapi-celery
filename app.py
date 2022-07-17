from fastapi import FastAPI
from models import init as init_db
from celery import Celery, current_app as current_celery_app

app = FastAPI()

init_db(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

celery: Celery = current_celery_app
celery.config_from_object("config.celery")
celery.autodiscover_tasks(["celery_tasks"])
