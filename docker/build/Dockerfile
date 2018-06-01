FROM alpine:3.7

# Set environment variables.
ENV LANG=en_US.UTF-8 \
    JAVA_ALPINE_VERSION=8.151.12-r0

# Install needed packages.
RUN apk add --no-cache \
    ca-certificates                 \
    openjdk8="$JAVA_ALPINE_VERSION" \
    maven

# Expose volumes.
#   /webapp     The directory containing the standard Maven tree, where we will
#               launch maven to build the sources and produce the artifacts.
VOLUME /webapp

# Default container running setup.
WORKDIR /webapp
ENTRYPOINT mvn clean package
