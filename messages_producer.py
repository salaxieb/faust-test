import faust
from preprocess import preprocess
import random


app = faust.App(
    'greetings_group',
    #broker='kafka://kafka:9093',
    broker='kafka://localhost:9092',
    #topic_partitions=4,
    autodiscover=True
)

# GUI для kafka: "kafkatool"
@app.timer(2.0)
async def publish_greetings():
    print('sending message')
    random_name = random.choice(['Vadim', 'Lena', 'Sergey', 'Ildar'])
    await preprocess.send(value={"name":random_name})
