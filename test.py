import unittest
from main import is_monotonic


class TestIsMonotonic(unittest.TestCase):
    def test_is_growing(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(is_monotonic(arr))

    def test_is_decreasing(self):
        arr = [5, 4, 3, 2, 1]
        self.assertTrue(is_monotonic(arr))

    def test_non_monotonic(self):
        arr = [1, 3, 2, 4, 5]
        self.assertFalse(is_monotonic(arr))

    def test_identical_elements(self):
        arr = [3, 3, 3, 3]
        self.assertTrue(is_monotonic(arr))
