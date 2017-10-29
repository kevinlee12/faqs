FROM python:latest

# Ensures that all prints are shown in the terminal
ENV PYTHONUNBUFFERED 1

# Install dockerize as a gatekeeper
RUN apt-get update && apt-get install -y wget
ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Add requirements file into working directory
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

# Update pip and install pip packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Move code into the working directory
ADD . /code/
