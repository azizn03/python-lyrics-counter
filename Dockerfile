FROM centos:7
RUN yum -y update && yum -y install curl \
    python3 \
    python3-pip \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip
RUN pip3 install musicbrainzngs
