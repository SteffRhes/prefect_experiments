FROM python:3.9.17
RUN pip install -U prefect==2.13.1
RUN mkdir /home/docker_user/
RUN useradd -u 1000 docker_user
RUN chown -R docker_user:docker_user /home/docker_user/
USER docker_user
WORKDIR /home/docker_user/
