import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(1)
        self.assertFalse(t_list.is_empty())

    def test_add(self):
        t_list = OrderedList()
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(11))
        self.assertTrue(t_list.add(12))
        self.assertTrue(t_list.add(13))
        self.assertTrue(t_list.add(7))
        self.assertTrue(t_list.add(9))
        self.assertFalse(t_list.add(10))
    
    def test_remove(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.remove(10))
        t_list.add(13)
        t_list.add(12)
        t_list.add(14)
        t_list.add(15)
        t_list.add(19)
        t_list.add(16)
        self.assertFalse(t_list.remove(100))
        self.assertTrue(t_list.remove(19))
        self.assertTrue(t_list.remove(12))
        self.assertTrue(t_list.remove(15))
    
    def test_index(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.index(10), 0)
        t_list.add(13)
        t_list.add(12)
        t_list.add(14)
        t_list.add(15)
        t_list.add(19)
        t_list.add(16)
        self.assertEqual(t_list.index(19), 6)
        self.assertEqual(t_list.index(15), 4)
        self.assertEqual(t_list.index(20), None)
    
    def test_pop(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
        t_list.add(13)
        t_list.add(12)
        t_list.add(14)
        self.assertEqual(t_list.pop(0), 12)
        t_list.add(15)
        t_list.add(19)
        t_list.add(16)
        self.assertEqual(t_list.pop(2),15)
        self.assertEqual(t_list.pop(3),19)
        with self.assertRaises(IndexError):
            t_list.pop(-1)
        with self.assertRaises(IndexError):
            t_list.pop(3)

    def test_search(self):
        t_list = OrderedList()
        self.assertFalse(t_list.search(14))
        t_list.add(10)
        t_list.add(13)
        t_list.add(12)
        self.assertTrue(t_list.search(13))
        self.assertFalse(t_list.search(14))
        t_list.add(14)
        self.assertTrue(t_list.search(10))
        t_list.add(15)
        t_list.add(19)
        self.assertTrue(t_list.search(14))
        t_list.add(16)
    def test_python_list(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(13)
        t_list.add(12)
        t_list.add(14)
        t_list.add(15)
        self.assertEqual(t_list.python_list(), [10, 12, 13, 14, 15])
        
    def test_python_list_reversed(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(13)
        t_list.add(12)
        t_list.add(14)
        t_list.add(15)
        self.assertEqual(t_list.python_list_reversed(), [15, 14, 13, 12, 10])

    def test_size(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(13)
        t_list.add(12)
        t_list.add(14)
        self.assertEqual(t_list.size(),4)

if __name__ == '__main__': 
    unittest.main()
