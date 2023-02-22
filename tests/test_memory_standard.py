import unittest
from .context import cache, standard

class TestLRUMemory(unittest.TestCase):
    def setUp(self):
        self.lru_memory = standard.LRU()

    def test_set_get_item(self):
        self.lru_memory['key'] = 'value'
        self.assertEqual(self.lru_memory['key'], 'value')

    def test_evict_regular(self):
        self.lru_memory[1] = 'one'
        self.lru_memory[2] = 'two'
        self.lru_memory.evict()

        self.assertTrue(1 not in self.lru_memory)
 
    def test_evict_recall(self):
        self.lru_memory[1] = 'one'
        self.lru_memory[2] = 'two'
        key_1 = self.lru_memory[1]
        self.lru_memory.evict()

        self.assertTrue(2 not in self.lru_memory)
    
    def test_evict_update(self):
        self.lru_memory[1] = 'one'
        self.lru_memory[2] = 'two'
        self.lru_memory[1] = 'one'
        self.lru_memory.evict()

        self.assertTrue(2 not in self.lru_memory)

class TestLIFOMemory(unittest.TestCase):
    def setUp(self):
        self.lifo_memory = standard.LIFO()

    def test_set_get_item(self):
        self.lifo_memory['key'] = 'value'
        self.assertEqual(self.lifo_memory['key'], 'value')

    def test_evict_regular(self):
        self.lifo_memory[1] = 'one'
        self.lifo_memory[2] = 'two'
        self.lifo_memory.evict()

        self.assertTrue(2 not in self.lifo_memory)

class TestFIFOMemory(unittest.TestCase):
    def setUp(self):
        self.fifo_memory = standard.FIFO()

    def test_set_get_item(self):
        self.fifo_memory['key'] = 'value'
        self.assertEqual(self.fifo_memory['key'], 'value')

    def test_evict_regular(self):
        self.fifo_memory[1] = 'one'
        self.fifo_memory[2] = 'two'
        self.fifo_memory.evict()

        self.assertTrue(1 not in self.fifo_memory)