Python offers built-in possibilities for caching, from a simple dictionary to a more complete data structure such as functools.lru_cache.
Those data structures are, however, by definition local to your Python process. 
When several copies of your application run across a large platform, using a in-memory data structure disallows sharing the cached content.
Therefore, when a system is distributed across a network, it also needs a cache that is distributed across a network.

I think that memcached is a good solution for distributed caching.
Memcached is available for many platforms such as Windows, MAC and Linux.

In order to interact with Memcached you’ll need to install a memcached client library. 
The preferred Python library for interacting with memcached is pymemcache

memcached is made of LRU, which determine when to throw out old data (if out of memory), or reuse memory.
All commands are implemented to be as fast and lock-friendly as possible. This gives allows near-deterministic query speeds for all use cases.
The time complexity for the commands is O(1)

You can simply install it using pip:
>>> pip install pymemcache

The following code shows how you can connect to memcached and use it as a network-distributed cache in your Python applications:

>>> from pymemcache.client import base

# Don't forget to run `memcached' before running this next line:
>>> client = base.Client(('localhost', 11211))

# Once the client is instantiated, you can access the cache:
>>> client.set('some_key', 'some value')

# Retrieve previously set data again:
>>> client.get('some_key')
'some value'

When storing data into memcached, you can set an expiration time—a maximum number of seconds for memcached to keep the key and value around. After that delay, memcached automatically removes the key from its cache.

References: 
https://realpython.com/python-memcache-efficient-caching/
https://github.com/memcached/memcached/wiki/Overview