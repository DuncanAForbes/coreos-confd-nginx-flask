FROM ubuntu:14.04

MAINTAINER Allan Costa <allaninocencio@yahoo.com.br>

RUN apt-get update
RUN apt-get install -y python-setuptools

# Install pip
RUN easy_install pip

# Install Flask
RUN pip install Flask

ADD server_start /usr/local/bin/server_start

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/server_start"]
