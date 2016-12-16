
from concurrent.futures import ThreadPoolExecutor

import time

from log import log

log(globals())

def wait_on_b():
    log('b function')
    log('b-->', globals())
    time.sleep(5)
    log(b.result())
    return 5

def wait_on_a():
    log('a function')
    log('a-->', globals())
    time.sleep(5)
    log(a.result())
    return 6

executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)



