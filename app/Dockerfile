FROM ubuntu:14.04
MAINTAINER Allan Costa <allaninocencio@yahoo.com.br>

RUN apt-get update
RUN apt-get --no-install-recommends install -y python-setuptools build-essential python-dev libpq-dev ca-certificates

# Install pip
RUN easy_install pip

ADD requirements.txt /tmp/requirements.txt

# Install requirements.txt
RUN pip install -r /tmp/requirements.txt

# Add app script
ADD app.py /home/app.py

EXPOSE 5000
WORKDIR /home/
ENTRYPOINT ["./app.py"]
