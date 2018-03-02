ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache \
  # py3-pip \
  # python3 \
  # python3-dev \
  # py-rpigpio
  python \
  py-pip \
  python-dev \
 && pip install RPi.GPIO

# Copy files for the python and bash scripts and set them as executable
COPY motor_test_copy.py /
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]