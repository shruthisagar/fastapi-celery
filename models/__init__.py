from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

DATABASE_NAME = "my_database"
DATABASE_PASSWORD = "default"
DATABASE_HOST = "database"
DATABASE_PORT = "5432"
DATABASE_USERNAME = "postgres"

TORTOISE_CONFIG: dict = {
    "connections": {
        "default" : f"postgres://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    },
    "apps":{
        "models":{
            "models":[
                "aerich.models",
                "models.first",
                "models.second"
            ],
            "default_connection": "default",
        }
    },
    "use_tz": True
}
generate_schemas = False

def init(app: FastAPI):
    register_tortoise(
        app, 
        TORTOISE_CONFIG,
        add_exception_handlers=True, 
        generate_schemas=generate_schemas
        )