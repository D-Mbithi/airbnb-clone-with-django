# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set enviromental variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install project dependancy
RUN pip install --upgrade pip
COPY ./requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .
