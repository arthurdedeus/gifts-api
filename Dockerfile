FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.7.1

WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock* /code/

RUN poetry install

COPY . /code/

EXPOSE 8000

CMD python manage.py collectstatic --no-input \
&& python manage.py migrate

