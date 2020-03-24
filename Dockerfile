# BASE 
FROM ubuntu:16.04

# METADATA
MAINTAINER Gregory Leeman gregoryleeman@outlook.com

# SYSTEM DEPENDENCIES
RUN \
	apt-get update --fix-missing \
	&& apt-get install -y wget bzip2 ca-certificates \
		git \
		build-essential \
		byobu \
		curl \
		git-core \
		htop \
		pkg-config \
		python3-dev \
		python-pip \
		python-setuptools \
		python-virtualenv \
		unzip \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# INSTALL PACKAGE
RUN \
	cd /home \
	&& git clone https://github.com/gregbioinf/hello_world.git \
	&& cd hello-world \
	&& python setup.py install \
	&& cd ..

RUN mkdir /ds
WORKDIR /ds
VOLUME /ds
ENV HOME=/ds
ENV SHELL=/bin/bash

# ENTRY POINT
CMD ["hello"]
