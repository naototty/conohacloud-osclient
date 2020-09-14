FROM ubuntu:trusty
MAINTAINER naoto.gohko@coha.tw

RUN apt-get update
## RUN apt-get install -y python-keystoneclient
## RUN apt-get install -y python-swiftclient
## RUN apt-get install -y python-novaclient
## RUN apt-get install -y python-troveclient
## RUN apt-get install -y python-glanceclient
## RUN apt-get install -y python-cinderclient
## RUN apt-get install -y python-heatclient
## RUN apt-get install -y python-ceilometerclient
## RUN apt-get install -y python-neutronclient

RUN wget https://downloads.rclone.org/rclone-current-linux-arm64.zip -O /usr/local/src/rclone-current-linux-arm64.zip && ( zcat /usr/local/src/rclone-current-linux-arm64.zip > /usr/local/bin/rclone ) && chmod +x /usr/local/bin/rclone
RUN curl -sL https://github.com/hironobu-s/novassh/releases/download/current/novassh-linux.amd64.gz | zcat > /usr/local/bin/novassh && chmod +x /usr/local/bin/novassh

