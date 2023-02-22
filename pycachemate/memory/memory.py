from abc import ABC, abstractmethod

class Memory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __setitem__(self, key):
        pass

    @abstractmethod
    def __getitem__(self, key, value):
        pass
    
    @abstractmethod
    def __contains__(self, key):
        pass

    @abstractmethod
    def evict(self):
        pass
