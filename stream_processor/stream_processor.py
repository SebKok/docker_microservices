import faust
import os
import random
from pymongo import MongoClient
from datetime import datetime

class Test(faust.Record):
    timestamp: str
    temperature: int

app = faust.App('temperature', broker='kafka://kafka:29092')
topic = app.topic('temperature', value_type=str)
client = MongoClient(host="host.docker.internal",port=27017, username="admin", password="admin")
db = client.admin

@app.agent(topic)
async def hello(messages):
    async for batch in messages.take(10, within=15):
        if os.environ['MODE'] == "MOVING_AVERAGE":
            average = sum(float(x['temperature']) for x in batch) / 10
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            db.temperature.insert_one({"average":average, "timestamp":timestamp})
            print('average: ' + str(average))
        elif os.environ['MODE'] == "RESERVOIR_SAMPLING":
            SAMPLE_SIZE = 3
            samples = []
            i = 0
            for item in batch:
                i += 1
                if len(samples) < SAMPLE_SIZE:
                    samples.append(item["temperature"])
                else:
                    rand = int(random.random() * i)
                    if rand < SAMPLE_SIZE:
                        samples[rand] = item["temperature"]
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            db.temperature.insert_one({"samples":samples, "timestamp":timestamp})
            print('timestamp: ' + timestamp + ' samples: ' + str(samples))
        else:
            raise SystemError()

if __name__ == '__main__':
    app.main()