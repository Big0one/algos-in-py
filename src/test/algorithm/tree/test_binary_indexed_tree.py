import unittest
from src.main.algorithm.tree.bit import *


class BinaryIndexedTreeTestCase(unittest.TestCase):
    def test_binary_indexed_tree(self):
        bit = BIT([1, 2, 3, 5, 6])
        bit.build()
        self.assertEqual(bit.query(3), 6)
        self.assertEqual(bit.query(4), 11)


if __name__ == "__main__":
    unittest.main()
