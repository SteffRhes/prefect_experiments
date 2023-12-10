#FROM python:3.9.17
#RUN pip install -U prefect==2.13.1
#RUN apt update
#RUN apt install -y sqlite3
FROM debian:12.0
RUN apt-get update
RUN apt-get install -qy curl
RUN curl -sSL https://get.docker.com/ | sh
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip install -U prefect==2.13.1 --break-system-packages
RUN pip install prefect-docker==0.3.11 --break-system-packages
RUN apt install -y sqlite3
RUN mkdir /home/docker_user/
RUN useradd -u 1000 docker_user
RUN chown -R docker_user:docker_user /home/docker_user/
#USER docker_user
WORKDIR /home/docker_user/
