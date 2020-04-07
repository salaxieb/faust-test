import faust
from time import sleep
from service import getResponseForText
import random
from multiprocessing import Pool
from reply import reply
from broker_detection import broker

class Message(faust.Record):
    name: str

app = faust.App(
    'greetings_group',
    broker=broker,
    autodiscover=True)

preprocess_topic = app.topic('preprocess_topic', value_type=Message)

@app.agent(preprocess_topic, concurrency=2)
async def preprocess(stream):
    async for message in stream:
        print('preprocessed ')
        await reply.send(value=message)
