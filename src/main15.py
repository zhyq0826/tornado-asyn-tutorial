"""
multi-threaded synchronous model
join方法的作用是阻塞主进程（挡住，无法执行join以后的语句），专注执行多线程。
多线程多join的情况下，依次执行各线程的join方法，前头一个结束了才能执行后面一个。
无参数，则等待到该线程结束，才开始执行下一个线程的join。
设置参数后，则等待该线程这么长时间就不管它了（而该线程并没有结束）。不管的意思就是可以执行后面的主进程了。
如果主线程还有其它的事情要做可以不join,
"""

from __future__ import print_function
import threading
import datetime
import time


def fun1():
    """
    task 1
    """
    print('fun1 start ' + str(datetime.datetime.now()))
    time.sleep(1)
    print('hello')
    print('fun1 end ' + str(datetime.datetime.now()))


def fun2():
    """
    task 2
    """
    print('fun2 start ' + str(datetime.datetime.now()))
    time.sleep(2)
    print('world')
    print('fun2 end ' + str(datetime.datetime.now()))


def fun3():
    """
    task 3
    """
    print('fun3 start ' + str(datetime.datetime.now()))
    time.sleep(3)
    print('!')
    print('fun3 end ' + str(datetime.datetime.now()))


if __name__ == '__main__':
    theads = []
    nloops = [fun1, fun2, fun3]
    start = time.time()

    for i in nloops:
        theads.append(threading.Thread(target=i))

    for i in theads:
        i.start()

    print('start join ')
    print(datetime.datetime.now())

    for i in theads:
        i.join(1)

    print('end join')
    print(datetime.datetime.now())

    print(time.time()-start)