FROM ubuntu:16.04
LABEL maintainer "jianyuan.ma@afconult.com"
LABEL Description="Robot Challenge Building Environment" Vendor="AF Technology" Version="1.1"


# ENVIRONMENT SETUP
# =================

ENV DEBIAN_FRONTEND=noninteractive

# INSTALLING TOOLS
# ================
COPY setup.sh /tmp/setup.sh
RUN chmod +x /tmp/setup.sh
RUN /tmp/setup.sh

RUN mkdir /etc/ros
RUN chmod a+rw -R /etc/ros

RUN adduser --disabled-password --gecos "" user
USER user

COPY envsetup.sh /tmp/envsetup.sh
ENTRYPOINT ["/tmp/envsetup.sh"]
