#!/bin/bash

set -eo pipefail

case "$KIND" in
    api)
        exec uvicorn app:app --proxy-headers --host 0.0.0.0 --port 80
    ;;
    celery_scheduler)
        exec celery -A app.celery beat -l INFO
    ;;
    celery_worker)
        exec celery -A app.celery worker -l INFO
    ;;
    celery_flower)
        exec celery -A app.celery flower -l INFO --port=5555
    ;;
    *)
        echo >&2 "invalid"
        exit 1
esac

    