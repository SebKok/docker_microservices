#!/bin/sh
set -x

python -m faust -A stream_processor worker -l info