from time import time

def sleep(t):
    """simple sleep function, which loads CPU"""
    start = time()
    s = 0
    while time() - start < t:
        for i in range(100_000):
            s += i

def getResponseForText(message):
    sleep(3)
    message = str(message)
    return 'hello, ' + message + '!'
