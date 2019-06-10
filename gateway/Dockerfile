FROM python:3-alpine
MAINTAINER Lucas Thisen <l.thiesen95@gmail.com> 

ENV FLASK_APP=/usr/src/app/app.py

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /usr/src/app

# Expose the Flask port
EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]