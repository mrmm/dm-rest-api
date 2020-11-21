FROM python:3-stretch
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt && chmod u+x scripts/*.sh \
    && useradd -ms /bin/bash django

USER django
ENTRYPOINT ["gunicorn", "-c", "gunicorn.py", "dm_api.wsgi"]
