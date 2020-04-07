import faust
from time import sleep
from service import getResponseForText
import random
from multiprocessing import Pool
from broker_detection import broker

class Message(faust.Record):
    name: str

app = faust.App(
    'greetings_group',
    broker=broker,
    autodiscover=True)


response_topic = app.topic('response_topic', value_type=Message)

@app.agent(response_topic)
async def reply(stream):
    async for message in stream:
        print('response', getResponseForText(message.name))
