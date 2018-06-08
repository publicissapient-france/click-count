FROM tomcat:8.5-jre8-alpine

LABEL maintainer "capuchon.dev@gmail.com"

# Set environment variables.
ENV LANG=en_US.UTF-8

# Copy the webapp to the tomcat container.
# It will be dezipped and run when tomcat will start.
COPY clickCount.war /usr/local/tomcat/webapps/
