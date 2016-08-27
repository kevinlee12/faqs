FROM heroku/python:3

# Ensures that all prints are shown in the terminal
ENV PYTHONUNBUFFERED 1

# Install dockerize as a gatekeeper
RUN apt-get update && apt-get install -y wget
ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Update pip
RUN pip install --upgrade pip
