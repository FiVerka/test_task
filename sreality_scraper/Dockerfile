# pull official base image
FROM python:3.9.17-bookworm
LABEL authors="fiverka"

# ENTRYPOINT ["top", "-b"]
# set work directory
WORKDIR /sreality_scraper

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 5432/tcp

CMD ["scrapy", "crawl", "flats"]