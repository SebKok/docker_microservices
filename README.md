Project made for Computer Systems Management class, AGH  
Author: Sebastian Kokoszka  
Topic: Dockerized application with mock tempearture sensor, RabbitMQ, Kafka, stream processing and MongoDB  

![Architecture](./Architecture.png)
1. temperature_sensor.py generates mock temperature data every second and sends it RabbitMQ queue 'temperature'
2. RabbitMQ Source Connector subscribes to queue 'temperature' and sends data to Kafka topic 'temperature'
3. Faust agent calcuates moving average or reservoir sampling and saves it to MongoDB  

**How to run**  
everything starts with from the docker-compose file  
> docker compose up -d