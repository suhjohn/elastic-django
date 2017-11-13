FROM suhjohn/base
MAINTAINER
MAINTAINER  johnsuh94@gmail.com

# Install JAVA
RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install software-properties-common
RUN apt-add-repository ppa:webupd8team/java
RUN apt-get update

RUN apt install oracle-java8-installer

# Install ES
RUN bash <(curl -s https://bitbucket.org/eunjeon/seunjeon/raw/master/elasticsearch/scripts/downloader.sh) -e 5.4.1 -p 5.4.1.1

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.4.1.tar.gz
RUN sha1sum elasticsearch-5.4.1.tar.gz
RUN tar -xzf elasticsearch-5.4.1.tar.gz


RUN cd elasticsearch-5.4.1
RUN ./bin/elasticsearch



# Install 은전한닢
