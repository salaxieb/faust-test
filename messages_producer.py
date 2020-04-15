import faust
from preprocess import preprocess
import random
from broker_detection import kafka_broker
from cassandra_utils import create_connection, get_all_greetings_counts

app = faust.App(
    'greetings_group',
    broker=kafka_broker,
    autodiscover=True)

@app.timer(2.0)
async def publish_greetings():
    print('sending message')
    random_name = random.choice(['Vadim', 'Lena', 'Sergey', 'Ildar'])
    await preprocess.send(value={"name":random_name})


from faust.web import Request, Response, View

@app.page('/count/')
class counter(View):
    session = create_connection()
    count: int = 0

    async def get(self, request: Request) -> Response:
        result = get_all_greetings_counts(self.session)
        print(result)
        return self.json(result)

    async def post(self, request: Request) -> Response:
        n: int = request.query['n']
        self.count += 1
        return self.json({'count': self.count})

    async def delete(self, request: Request) -> Response:
        self.count = 0
