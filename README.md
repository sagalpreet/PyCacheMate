# PyCacheMate
This is an in-memory caching library in python for general-purpose use.

### Standard Eviction Policies
Standard eviction policies like LRU, FIFO and LIFO are efficiently implemented and can be readily used.

### Custom Eviction Policies
Custom eviction policies can be defined by extending the `Memory` class from `memory` module.

### Cache Wrapper
The `Cache` class acts like a wrapper over the `Memory` classes which define eviction policies. Thread safety is taken care of at higher level, so the lower level implementation of eviction policies need not worry about the thread safety.

### Setup the library
```
make init
```

### Run Unit Tests
```
make test
```

### Use the library
To use the cache functionality,
```python
from pycachemate.cache import Cache

# the default eviction policy is LRU
cache = Cache()
```

To use standard eviction policies
```python
from pycachemate.cache import Cache
from pycachemate.memory.standard import FIFO, LIFO

cache = Cache(memory = FIFO(), capacity = 100)
```

To define custom eviction policies
```python
from pycachemate.cache import Cache
from pycachemate.memory.memory import Memory

class CustomMemory(Memory):
    # implement all the required methods here
    pass

cache = Cache(memory = CustomMemory(), capacity = 100)
```

### TODO
The docs need to be added.