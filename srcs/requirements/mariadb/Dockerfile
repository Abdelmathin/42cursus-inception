FROM debian:stable

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python && mkdir -p /etc/mysql

COPY tools/setup.py /etc/mysql

CMD ["/usr/bin/python", "/etc/mysql/setup.py"]
