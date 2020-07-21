import unittest
from src.main.algorithm.sorting import *


class SortingTest(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        
    
    def test_selection_sort(self):
        self.assertEqual(selection_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
        
        
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort( [64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    
if __name__ == "__main__":
    unittest.main()