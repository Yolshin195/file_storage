#!/bin/bash

python /file_storage/docker/wait_for_postgres.py

alembic upgrade head

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000