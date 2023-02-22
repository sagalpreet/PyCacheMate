import unittest
from .context import cache

class TestCacheMethods(unittest.TestCase):
    def setUp(self):
        self.lru_cache = cache.Cache(capacity = 10)

    def test_set_get_item(self):
        self.lru_cache['key'] = 'value'
        self.assertEqual(self.lru_cache['key'], 'value')

    def test_capacity(self):
        for num in range(11):
            self.lru_cache[num] = 2 * num
        self.assertTrue(0 not in self.lru_cache)

    def test_size(self):
        for num in range(11):
            self.lru_cache[num] = 2 * num
            self.assertEqual(len(self.lru_cache), min(num + 1, 10))