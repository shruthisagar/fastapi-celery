broker_url = f"amqp://guest:guest@rabbitmq:5672//"
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "UTC"
enable_utc = True

task_track_started = True
task_publish_retry = False

beat_schedule = {
    "task_1": {
        "task": "app.celery_tasks.tasks.task_1",
        "schedule": 20
    }
}