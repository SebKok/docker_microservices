import faust

class Test(faust.Record):
    timestamp: str
    temperature: int

app = faust.App('myapp', broker='kafka://localhost:9092')
topic = app.topic('temperature', value_type=str)


@app.agent(topic)
async def hello(messages):
    async for message in messages:
        print(f'Received {message}')


if __name__ == '__main__':
    app.main()