import os

SECRET_KEY = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)
if SECRET_KEY:
    print('I am running in a Docker container')
    broker = 'kafka://kafka:9093'
else:
    print('I amd running on local enterpreter')
    broker = 'kafka://localhost:9092'
