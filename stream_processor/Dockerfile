FROM python:3.9

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

ADD . /stream_processor
WORKDIR /stream_processor
RUN pip install -r requirements.txt

RUN apt-get install -y netcat && apt-get autoremove -y

ENTRYPOINT ["./wait_for_kafka.sh"]

CMD ["./start_faust.sh"]