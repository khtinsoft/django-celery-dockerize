FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1
ENV PPYTHONENCODING utf-8

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get update -y

RUN apt-get install -y build-essential python3 python3-dev python3-pip      
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y language-pack-ko
RUN apt-get install -y gettext
RUN apt-get install -y nginx

RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8
RUN locale-gen ko_KR.UTF-8
RUN ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel

ADD . /sample-project/sample-project
WORKDIR /sample-project/sample-project
RUN pip3 install -r requirements.txt