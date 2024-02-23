#!/bin/sh

# Exit script in case of error
set -e

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Applying database migrations..."
python manage.py migrate

# Start Gunicorn or any other web server you are using
# Example for Gunicorn:
 gunicorn settings.wsgi:application --bind 0.0.0.0:8000

# If you're using Django's development server, you can start it like this:
#exec python manage.py runserver 0.0.0.0:8000
