from .memory.memory import Memory
from .memory.standard import LRU
from threading import Lock
from typing import Hashable

class Cache:
    def __init__(self, memory = LRU(), capacity = None):
        """
        Initialize the cache with the type of memory (eviction policy)
        to be used and the capacity of the cache.
        If the capacity is set to None, then no eviction happens.

        Parameters:
            memory (Memory): Type of memory (eviction policy) used.
            capacity (int): The maximum size of the cache.
        """

        assert isinstance(memory, Memory), f"memory must be of type {Memory}, {type(memory)} detected instead"
        assert isinstance(capacity, int) or capacity == None, f"capacity must be an integer, {type(capacity)} detected instead"

        self.__mem = memory
        self.__capacity = capacity
        self.__size = 0
        self.__lock = Lock()
    
    def __getitem__(self, key):
        """
        The method returns the value corresponding to key if cached else raises an exception.

        Parameters:
            key (hashable): The key for which value needs to be fetched from the cache.

        Returns:
            value: The value corresponding to the key from the cache.

        Raises KeyError: If the key is not found in the cache.
        """

        assert isinstance(key, Hashable), f"{key}: {type(key)} is not hashable"

        try:
            with self.__lock:
                return self.__mem[key]
        except KeyError as k:
            raise KeyError(f"Key value {key} does not exist in the cache")

    def __setitem__(self, key, value):
        """
        The method stores the value corresponding to the key in the cache while maintaining its max size.

        Parameters:
            key (hashable): The key for which value needs to be fetched from the cache.
            value: The value to be stored corresponding to the key in the cache.

        Returns:
            None
        """

        assert isinstance(key, Hashable), f"{key}: {type(key)} is not hashable"

        with self.__lock:
            if (self.__size == self.__capacity):
                self.__mem.evict()
                self.__size -= 1

            self.__mem[key] = value
            self.__size += 1

    def __len__(self):
        """
        The method to get the current size of the cache.

        Parameters:
        
        Returns:
            int: The number of key-value pairs in the cache.
        """

        with self.__lock:
            return self.__size
        
    def __contains__(self, key):
        """
        The method to check if some key exists in the cache.

        Parameters:
            key (hashable): The key to be searched for in the cache.

        Returns:
            bool: True if the key exists else False.
        """

        assert isinstance(key, Hashable), f"{key}: {type(key)} is not hashable"

        with self.__lock:
            return key in self.__mem