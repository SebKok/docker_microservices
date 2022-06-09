FROM python:3
ADD . /temperature_sensor
WORKDIR /temperature_sensor
RUN pip install -r requirements.txt
CMD ["python", "temperature_sensor.py"]