import os
DATABASE_USERNAME = os.getenv("DB_HOST")
DATABASE_PASSWORD = os.getenv("DB_PASS")
DATABASE_NAME = os.getenv("DB_NAME")
DATABASE_PORT = os.getenv("DB_PORT",5432)
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)
