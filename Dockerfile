FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /code

USER appuser

EXPOSE 8000

CMD python manage.py collectstatic --no-input && \
    python manage.py migrate && \
    gunicorn -b 0.0.0.0:8000 settings.wsgi
