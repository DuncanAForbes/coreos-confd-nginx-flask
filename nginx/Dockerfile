FROM ubuntu:14.04
MAINTAINER Allan Costa <allaninocencio@yahoo.com.br>

RUN apt-get update

# Install NGINX
RUN apt-get install nginx curl -y

# Install confd
RUN curl -L https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-amd64 -o confd
RUN chmod +x confd
RUN cp confd /usr/local/bin/confd

# Add files
ADD nginx.toml /etc/confd/conf.d/nginx.toml
ADD nginx.conf.tmpl /etc/confd/templates/nginx.conf.tmpl
ADD confd-watch /usr/local/bin/confd-watch

# Remove default NGINX config file
RUN rm /etc/nginx/sites-enabled/default

ENTRYPOINT ["/usr/local/bin/confd-watch"]
