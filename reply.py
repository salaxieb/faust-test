import faust
from time import sleep
from service import getResponseForText
import happybase as hb
import random
from multiprocessing import Pool

class Message(faust.Record):
    name: str

app = faust.App(
    'greetings_group',
    #broker='kafka://kafka:9093',
    broker='kafka://localhost:9092',
    #topic_partitions=4, #setting defines the maximum number of workers we can distribute the workload to
    #value_serializer='raw',
    #autodiscover=True)
    )


response_topic = app.topic('response_topic')

@app.agent(response_topic, concurrency=2)
async def reply(stream):
    #pool = Pool(processes=4)
    async for message in stream:
        #result = pool.apply(getResponseForText, message)
        #print(result.successful())
        #     #print(message['name'])
        print('response')
        print(getResponseForText(message))
