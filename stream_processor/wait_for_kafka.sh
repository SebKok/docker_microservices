#!/bin/bash
set -e

cmd="$@"

until nc -vz ${KAFKA_BOOTSTRAP_SERVER_NAME} ${KAFKA_BOOTSTRAP_SERVER_PORT}; do
    >&2 echo "Waiting for Kafka to be ready..."
    sleep 2
done
echo "Executing command ${cmd}"
exec $cmd