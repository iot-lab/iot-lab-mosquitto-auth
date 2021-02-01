FROM python:3.8-slim

LABEL maintainer="admin@iot-lab.info"

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install flask requests

COPY main.py /usr/local/bin/
COPY run.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run.sh

EXPOSE 5000

ENTRYPOINT ["run.sh"]
