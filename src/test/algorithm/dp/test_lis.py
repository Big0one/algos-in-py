import unittest
from src.main.algorithm.dp.lis import *


class LISTestCase(unittest.TestCase):
    def test_lis(self):
        self.assertEqual(lis([3, -2, 3, 1, 2, 5, 2, 4]), [-2, 1, 2, 4])


if __name__ == "__main__":
    unittest.main()
