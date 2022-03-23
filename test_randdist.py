# test_randdist.py
import randdist
import unittest
class TestRanddist(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(randdist.add(1, 2), 3)
if __name__ == '__main__':
    unittest.main()