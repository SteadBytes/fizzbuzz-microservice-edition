FROM python:3.7-slim

RUN pip install Flask requests gunicorn

EXPOSE 5000

COPY services /services

WORKDIR /services

ENTRYPOINT [ "/bin/bash", "start.sh" ]

