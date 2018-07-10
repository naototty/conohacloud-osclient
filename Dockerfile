FROM ubuntu:trusty
MAINTAINER chroum@gmail.com

RUN apt-get update
RUN apt-get install -y python-keystoneclient
RUN apt-get install -y python-swiftclient
RUN apt-get install -y python-novaclient
RUN apt-get install -y python-troveclient
RUN apt-get install -y python-glanceclient
RUN apt-get install -y python-cinderclient
RUN apt-get install -y python-heatclient
RUN apt-get install -y python-ceilometerclient
RUN apt-get install -y python-neutronclient
RUN wget https://downloads.rclone.org/rclone-current-linux-arm64.zip -O /usr/local/src/rclone-current-linux-arm64.zip

