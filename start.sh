#!/bin/bash
export PORT=${PORT:-8080}  # Railpack sets PORT
export PYTHONUNBUFFERED=1

# Activate virtualenv if using one
# source venv/bin/activate

# Run Django server
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn myapp.wsgi:application --bind 0.0.0.0:$PORT
