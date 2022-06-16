FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api
COPY requirements/production.txt ./
RUN pip install -r requirements/production.txt
COPY . ./
EXPOSE 8000
