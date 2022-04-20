# this is used to build image for the rabbit to kafka connector
FROM confluentinc/cp-kafka-connect-base:5.2.1
RUN confluent-hub install confluentinc/kafka-connect-rabbitmq:latest --no-prompt