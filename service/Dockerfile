FROM python:3-stretch
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt && chmod u+x scripts/*.sh
ENTRYPOINT ["gunicorn", "-c", "gunicorn.py", "dm_api.wsgi"]
