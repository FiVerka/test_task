# pull official base image
FROM python:3.9.17-bookworm
LABEL authors="fiverka"

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

# CMD ["flask", "run"]
CMD ["python", "app.py"]