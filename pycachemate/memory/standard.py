from .memory import Memory
from collections import OrderedDict

class LRU(Memory):
    """
    Memory with Least Recently Used eviction policy.
    When the cache is full to its capacity and a new key is inserted,
    the least recently referred key is removed.
    """
    def __init__(self):
        super().__init__()
        self.__mem = OrderedDict()
    
    def __setitem__(self, key, value):
        self.__mem[key] = value
        self.__mem.move_to_end(key)

    def __getitem__(self, key):
        self.__mem.move_to_end(key)
        return self.__mem[key]
    
    def __contains__(self, key):
        return key in self.__mem
    
    def evict(self):
        self.__mem.popitem(last = False)

class LIFO(Memory):
    """
    Memory with Last In First Out eviction policy.
    When the cache is full to its capacity and a new key is inserted,
    the most recently inserted key is removed.
    """
    def __init__(self):
        super().__init__()
        self.__mem = OrderedDict()
    
    def __setitem__(self, key, value):
        self.__mem[key] = value
        self.__mem.move_to_end(key)

    def __getitem__(self, key):
        return self.__mem[key]
    
    def __contains__(self, key):
        return key in self.__mem
    
    def evict(self):
        self.__mem.popitem(last = True)


class FIFO(Memory):
    """
    Memory with First In First Out eviction policy.
    When the cache is full to its capacity and a new key is inserted,
    the earliest inserted key is removed.
    """
    def __init__(self):
        super().__init__()
        self.__mem = OrderedDict()
    
    def __setitem__(self, key, value):
        self.__mem[key] = value
        self.__mem.move_to_end(key)

    def __getitem__(self, key):
        return self.__mem[key]
    
    def __contains__(self, key):
        return key in self.__mem
    
    def evict(self):
        self.__mem.popitem(last = False)