FROM python:3
MAINTAINER Stefan Schindler

RUN apt-get update
RUN apt-get install -y libenchant1c2a libaspell-dev locales

RUN useradd -m -d /home/sopel sopel
WORKDIR /home/sopel

RUN pip install IPython icalendar BeautifulSoup4 lxml numpy
RUN pip install git+https://github.com/sopel-irc/sopel.git
RUN echo "fr_FR.UTF-8 UTF-8" > /etc/locale.gen
RUN update-locale
RUN dpkg-reconfigure locales -f noninteractive

VOLUME /home/sopel/.sopel

USER sopel
CMD sopel
