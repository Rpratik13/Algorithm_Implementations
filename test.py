import unittest
from linearSearch import *

class TestLinearSearch(unittest.TestCase):
    def testSearch(self):
        array = [4, 5, 0, 1, 10, 11, 15]
        self.assertEqual(linearSearch(array, 10), 4)


if __name__ == '__main__':
    unittest.main()
