FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.7.0

WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /code/

EXPOSE 8000

CMD python manage.py collectstatic --no-input \
&& python manage.py migrate \
&& gunicorn settings.wsgi:application --bind 0.0.0.0:8000


#COPY entrypoint.sh /code/entrypoint.sh
#
#RUN chmod +x /code/entrypoint.sh
#
#
#ENTRYPOINT ["/code/entrypoint.sh"]