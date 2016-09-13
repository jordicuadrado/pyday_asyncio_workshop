Content
=======

* About me
* Asyncio basics
* Currency converter HTTP client.
* TDD in an asynchronous world
* Coverage of your Currency converter
* Currency converter as a web resource
* Part 2

----

About me
========

* Pau Freixes `@pfreixes <https://twitter.com/pfreixes>`_, `git <https://github.com/pfreixes>`_
* Senior Software Enginner at SkyScanner
* Member of the Hotels Backend Squad
* One recomendation: read the others code, learn from the maters

----

Asyncio basics: basic theory
============================

- Implements the best practices from other frameworks `Twisted`, `Tornado`, etc.
- Concurrence via coroutines, can be paused and rescheduled  
- First implementation via iterators, since 3.5 as an internal and specific implementation.
- Designed to build other frameworks upon it. `Tornado with Asyncio <http://www.tornadoweb.org/en/stable/asyncio.html>`_

----

Asyncio basics: Coroutine
=========================

- A special Python function: with the `async def` statement or the `@asyncio.coroutine` decorator 

.. code-block:: python 

    import asyncio

    async def do_something():
        await asyncio.sleep(1)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_something())

----

Asyncio basics: Coroutine
=========================

- Calling a coroutine does not start the code automatically: `await` and `yield from` do that implicitly.
- Once paused it is rescheduled by the loop because of a I/O event, by time, etc.
- Magic methods **can not** be defined as coroutines : `__init__`, `__cmp__`, etc


----

Asyncio basics: Coroutine
=========================

If **foo** calls a coroutine and waits for the result, it becomes a croutine.

.. code-block:: python 

    async def bar():
        await asyncio.sleep(1)
        return 1 + 1

    async def foo():
        result = await bar()

----

Asyncio basics: Future
======================

Intermediate object to set results in the past and gather them into the Future

.. code-block:: python 

    from time import sleep

    def foo(f):
        sleep(1)
        f.set_result(10)

    f = asyncio.Future()
    foo(f)
    f.result()

----

Asyncio basics: Future
======================

**Damm it**, this is not asynchronous. What is going on?.

*Future* should be treated as a **synchronization object, used by a consumer and producer**.

As an example have a look to the code to `set the results <https://github.com/python/cpython/blob/master/Lib/asyncio/futures.py#L284>`_.

----

Asyncio basics: Future
======================

The `await` expression is compatible with futures.

.. code-block:: python 

    def bar():
        f = asyncio.Future()
        f.set_result(10)
        return f

    async def foo():
        result = await bar()
        print(result)

----

Asyncio basics: Future
======================

We will come later, no worries :/

----

Asyncio basics: Task
====================

- Unit of a concurrent asynchronous work.
- As an example each HTTP request is handled as a task by `aiohttp`.
- Calling `ensure_future` giving a coroutine as a param it starts a new task.

----

Asyncio basics: Task
====================

Running many tasks concurrently

.. code-block:: python 

    async def task(i):
        await asyncio.sleep(1)
        return i + 1

    async def foo():
        task = asyncio.ensure_future(task(10))
        return await asyncio.gather(*[task])

----

Asyncio basics: Task
====================

A **Task** is a subclass of `Future <https://github.com/python/cpython/blob/master/Lib/asyncio/tasks.py#L243>`_. Why not
use the callback system ?

.. code-block:: python 

    async def task(i):
        await asyncio.sleep(1)
        return i + 1

    def callback(future):
        pritn(future.results())

    def foo():
        task = asyncio.ensure_future(task(10))
        task.add_done_callback(callback)

----

Asyncio basics: Recaping
========================

- **Coroutines** as a way to get concurrence.
- **Futures** as a way to pick up results in the future once are available.
- **Tasks** unit of concurrency.

----


Time for coding
===============

Prepare your enviornment

.. code-block:: bash

    $ git clone\
    https://github.com/Skyscanner/pyday_asyncio_workshop.git
    $ cd pyday_asyncio_workshop.git
    $ mkvirtualenv -p python3
    $ pip install -r requirements.txt

----

Currency converter HTTP client.
===============================

Implement a HTTP client to convert an amount of money from EUR to another currency

What do we expect ?

.. code-block:: bash

    $ python currency/client.py USD 100
    122 USD

----

Currency converter HTTP client.
===============================

- Use the template behind the path `/currency/client.py`
- Use the `ClientSession`, more info `here <http://aiohttp.readthedocs.io/en/stable/client.html>`_
- Use the following API REST endpoint : http://api.fixer.io/latest

----

Currency converter HTTP client.
===============================

You have **10 minutes**. Just fill the code gaps, have fun!

----

TDD in an asynchronous world
============================

As you do usually but with some considerations

.. code-block:: python 

    def test_foo():
        async def _():
            assert await foo() == 10
        asyncio.get_event_loop().runt_until_complete(_())


----

TDD in an asynchronous world
============================

But we can get some help from `pytest.asyncio`

.. code-block:: python 

    @pytest.mark.asyncio
    def test_foo():
        assert await foo() == 10

----


Currency converter test
=======================

What are we going to do ? Put a fence arround the `convert` function
to test it and get a deterministic behaviour.

How will we do that? Creating an asyncronous fixture and patching
the `get` method to return this fixture.

----

Currency converter test
=======================

The result expected is :

.. code-block:: bash

    $ pytest -q  tests/currency/
    .
    1 passed in 0.02 seconds

----


Currency converter test
========================

- Use the template behind the path `/test/currency/test_client.py`


----

Currency converter HTTP client.
===============================

You have **10 minutes**. Just fill the code gaps, have fun!

----


Aiohttp the asynchronous webserver
==================================

- Build upon asyncio
- Meets the basic requirements for a HTTP server : sessions, cookies, etc.
- Comes with support for Websockets.
- More info here : `http://aiohttp.readthedocs.io <http://aiohttp.readthedocs.io/en/stable/>`_

----

Aiohttp the asynchronous webserver
==================================

The minimal python code needed:

.. code-block:: python

    from aiohttp import web

    async def hello(request):
        return web.Response(body=b"Hello, world")

    app = web.Application()
    app.router.add_route('GET', '/', hello)
    web.run_app(app)


----

Currency converter as a web resource
====================================

Implement a HTTP server that exposes the currency converter as an endpiont.

What do we expect ?

.. code-block:: bash

    $ python webserver.py &
    $ curl http://localhost:8080/convert/GBP/100
    GBP 88.4

----

Currency converter as a web resource
====================================

- Use the template behind the path `webserver.py`
- More info `here <http://aiohttp.readthedocs.io/en/stable/web.html>`_

----

Currency converter as a web resource
====================================

You have **10 minutes**. Just fill the code gaps, have fun!

----
