FROM python:3
RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./db /app/db
COPY ./models /app/models
COPY ./static /app/static
COPY ./templates /app/templates
COPY ./web /app/web
COPY flask_app.py /app
ENV MongoHost 127.0.0.1
ENV MongoPort 27017
ENV FLASK_APP flask_app.py
CMD flask run --host=0.0.0.0 --port=$FLASK_PORT