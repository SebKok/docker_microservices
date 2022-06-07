import faust
from pymongo import MongoClient
from datetime import datetime

class Test(faust.Record):
    timestamp: str
    temperature: int

app = faust.App('myapp', broker='kafka://localhost:9092')
topic = app.topic('temperature', value_type=str)
client = MongoClient(port=27017, username="admin", password="admin")
db = client.admin

@app.agent(topic)
async def hello(messages):
    async for batch in messages.take(5, within=10):
        average = sum(float(x['temperature']) for x in batch) / 5
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.temperature.insert_one({"average":average, "timestamp":timestamp})
        print('average: ' + str(average))


if __name__ == '__main__':
    app.main()