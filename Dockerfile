FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app

# Copy requirements.txt alone first to leverage docker caching on dependencies
COPY requirements.txt requirements.txt

# Install python modules. Also add build tools since some dependencies want to compile code
RUN apk add --no-cache build-base libffi-dev \
    && apk add --no-cache bash \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apk del --no-cache build-base libffi-dev

# Copy related files to working directory
# COPY celery_tasks celery_tasks

# COPY config config

# COPY models models

# COPY __init__.py __init__.py

# COPY app.py app.py



# Make entrypoint executable and run
COPY docker-entrypoint.sh /bin/
RUN chmod +x /bin/docker-entrypoint.sh
CMD ["docker-entrypoint.sh"]