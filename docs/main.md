### main01

示例中使用**同步**调用的方式执行了两次请求, 一个执行完成之后，才能继续执行另一个。HTTPClient 是同步 client，完成请求之后通过 callback 进行通知。

同步是最常见也是最符合程序员思维逻辑的调用方式。

### main02

示例中使用**异步**调用的方式执行了两次请求, 两个的执行完成顺序是不确定的。AsyncHTTPClient 是异步 client，完成这异步请求必须要借助 ioloop 进行相应的事件监听，完成请求之后通过 callback 进行通知。

由于是异步执行，执行完成的时间取决于当前执行的操作，在例子中，优先显示结果的是响应速度更快的请求。

对比 main01 的执行时间，main02 的执行时间稍微短一些(多次执行统计平均值)。

### main03

示例中的异步调用返回的是一个 future，为 future 注册一个调用完成之后的回调函数，future 执行完成之后，回调函数被执行，参数是一个状态为 done 的 future。

**如何理解 future ？**

https://tornado.readthedocs.io/en/stable/concurrent.html#tornado.concurrent.Future

A Future encapsulates the result of an asynchronous operation. In synchronous applications Futures are used to wait for the result from a thread or process pool; in Tornado they are normally used with IOLoop.add_future or by yielding them in a gen.coroutine

future 代表一次异步的执行。在同步应用程序中，furure 用来等待从一个线程或进程池执行的操作结果，在 tornado 中他们常被 ioloop.add_future 使用或者在 coroutine 中被 yield。

future 可以有不同的状态来表明当前执行的状况什么，future 也可以对执行进行相应的控制操作，比如挂起(suspend)，中断(cancel)，停止(stop)等。


### main04

https://tornado.readthedocs.io/en/stable/gen.html

示例通过 tornado 实现的 coroutine 装饰器返回 future，这样可以像写同步的方式来实现异步的执行，代码可读性更强，更容易理解。

在 coroutine 中 yield 一个 future 对象，将得到 future 的执行结果。

借助于 coroutine，开发者可以告别 callback 的方式写异步代码。

Most asynchronous functions in Tornado return a Future; yielding this object returns its result.

tornado 中的异步函数大部分都返回 future 对象，yield 这个 future 就能得到 future 的 result.

Functions with this decorator return a Future. Coroutines may “return” by raising the special exception Return(value)

coroutine 装饰器会让调用函数（生成器函数）返回 future，在调用函数中返回值，可以使用 gen.Return。


### main05

如果异步调用的函数中有阻塞操作，可以借助多线程来执行并返回对应的 future ，yield future 将得到 future 的执行结果，再借助 gen.Return 返回结果到调用者 caller。

在 coroutine 装饰的函数中，yield 对象必须是个 future，而且这个 future 必须要能够解析或者在适当的时候失败，不然这个 future 将一直挂起

### main06

https://tornado.readthedocs.io/en/stable/guide/coroutines.html

示例展示了 coroutine 中的异常处理

Coroutines do not raise exceptions in the normal way: any exception they raise will be trapped in the Future until it is yielded. This means it is important to call coroutines in the right way, or you may have errors that go unnoticed

coroutine 不会以常规的方式抛出异常，异常只有在 future is yielded 时才会出现，如果不注意 coroutine 的使用方式，可能会错过异常

比如示例中的 bad_call 调用，看不到异常的出现。

In nearly all cases, any function that calls a coroutine must be a coroutine itself, 
and use the yield keyword in the call

注意在任何调用 coroutine 的函数本身必须是 coroutine，而且要在调用中使用 yield ，示例中 good_call 中调用 divide ，那么 good_call 本身也必须是 coroutine。

https://tornado.readthedocs.io/en/stable/concurrent.html#consumer-methods

如果发生异常，调用 future.result 会再次把异常抛出，如果调用 future exception 则只是返回异常



