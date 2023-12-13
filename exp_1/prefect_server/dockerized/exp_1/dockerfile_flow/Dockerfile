FROM alpine:3.18.2
# If the docker service should not be run as root, a non-root user must be defined in the Dockerfile
RUN adduser -D docker_user
USER docker_user
CMD ["cat", "/etc/os-release"]
