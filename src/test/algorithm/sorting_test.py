import unittest
from src.main.algorithm.sorting import *


class DictTest(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(
            bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90]
        )

    def test_selection_sort(self):
        self.assertEqual(
            selection_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90]
        )

    def test_insertion_sort(self):
        self.assertEqual(
            insertion_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90]
        )

    def test_quick_sort(self):
        array = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(
            quick_sort(array, 0, (len(array) - 1)), [11, 12, 22, 25, 34, 64, 90]
        )

    def test_merge_sort(self):
        array = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(
            merge_sort(array, 0, len(array) - 1), [11, 12, 22, 25, 34, 64, 90]
        )

        array = [12, 11, 13, 5, 6, 7]
        self.assertEqual(merge_sort(array, 0, len(array) - 1), [5, 6, 7, 11, 12, 13])
