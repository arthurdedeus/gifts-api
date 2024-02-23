FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.7.0

WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

ECHO "Collecting static files..."
RUN python manage.py collectstatic --no-input

ECHO "Applying database migrations..."
RUN python manage.py migrate

ECHO "Starting up server"
RUN python manage.py runserver 0.0.0.0:8000

#COPY entrypoint.sh /code/entrypoint.sh
#
#RUN chmod +x /code/entrypoint.sh
#
#COPY . /code/
#
#ENTRYPOINT ["/code/entrypoint.sh"]