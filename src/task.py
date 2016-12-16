from celery import Celery
import time

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@app.task
def add(x, y):
    time.sleep(3)
    return x + y