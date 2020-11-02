import unittest
from main import max_number
from main import descending_sort

class TestMaxNumbers(unittest.TestCase):
    def test_max_numbers(self):
        assert max_number([3, 5, 6, 9, 12, 78]) == 78, "The max number in [[3, 5, 6, 9, 12, 78]"

    def test_descending_order_sorter(self):
        assert descending_sort([10, 6, 5, 18]) == [18, 10, 6, 5], "The order in [10, 6, 5, 18] should be [18, 10, 6, 5]"
