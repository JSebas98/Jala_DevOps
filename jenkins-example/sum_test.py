import unittest
# Import sum_iterable from my_sum.py
from my_sum import sum_iterable

class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that the function can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum_iterable(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()

