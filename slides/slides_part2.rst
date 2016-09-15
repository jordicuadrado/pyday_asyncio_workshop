Content
=======

* Futures and Threads
* Synchronous Currency converter made asynchronous
* The Flask implementation
* Comparing the three implementations

----

Futures and Threads
===================

Remember about the `Futures`, its a way to synchronize Producers and Consumers.

.. code-block:: python 
    
    async def poll(buffer):
        correlation_id, data = parse_buffer(buffer)
        future.pop(correlation_id).set_result(data)

    async def some_operation(request):
        f = Future()
        correlation_id = uuid()
        futures.append(f)
        send_noneblocking(pack(correlation_id, request))
        return f

    result = await some_opeation(request)


----

Futures and Threads
===================

Asyncio implements a way to wrap threads executors in a Future.

.. code-block:: python 

    def bar():
        return 10

    async def foo()
        executor = ThreadPoolExecutor()
        await asyncio.get_event_loop().run_in_executor(executor, bar)

    result = await foo()

----

Futures and Threads
===================

This is a way, the easy one, to wrap synchronous code and execute it
asynchronoysly. Also a proper way to run CPU bound functions.

----

Time for coding
===============

Prepare your enviornment

.. code-block:: bash

    $ git checkout part2
    $ pip install -r requirements.txt

Synchronous Currency converter made asynchronous
================================================

Implement a HTTP server that exposes the currency converter synchronous 
wraped to be executed asynchronoysly.

What do we expect ?

.. code-block:: bash

    $ python webserver_forceasync.py &
    $ curl http://localhost:8080/convert/GBP/100
    GBP 88.4

----

Synchronous Currency converter made asynchronous
================================================

- Use the template behind the path `webserver_forceasync.py`
- More info about `threadpoolexecutor <https://docs.python.org/3/library/concurrent.futures.html>`_ and `run_in_executor <https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop.run_in_executor>`_

----

Synchronous Currency converter made asynchronous
================================================

You have **10 minutes**. Just fill the code gaps, have fun!

----
