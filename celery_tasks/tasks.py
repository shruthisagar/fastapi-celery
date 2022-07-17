from logging import getLogger
from app import celery
logger = getLogger("task_logger")

@celery.task()
def task_1():
    logger.log("This is a simple task")
