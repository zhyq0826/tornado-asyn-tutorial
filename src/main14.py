"""
single-threaded synchronous model
"""

from __future__ import print_function
import time


def fun1():
    """
    task 1
    """
    time.sleep(1)
    print('hello')


def fun2():
    """
    task 2
    """
    time.sleep(2)
    print('world')


def fun3():
    """
    task 3
    """
    time.sleep(3)
    print('!')


if __name__ == '__main__':
    start = time.time()
    fun1()
    fun2()
    fun3()
    print(time.time() - start)
