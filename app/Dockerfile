FROM ubuntu:14.04
MAINTAINER Allan Costa <allaninocencio@yahoo.com.br>

RUN apt-get update
RUN apt-get install -y python-dev libssl-dev python-setuptools  libffi-dev build-essential

# Install pip
RUN easy_install pip

ADD requirements.txt /tmp/requirements.txt

# Install requirements.txt
RUN pip install -r /tmp/requirements.txt

# Add app script
ADD app.py /home/app.py

EXPOSE 5000
WORKDIR /home/
CMD ["./app.py"]
