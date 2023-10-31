import unittest
from python_Add import add

class test_Add_Positive(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 5), 8)

if __name__ == '__main__':
    unittest.main()
