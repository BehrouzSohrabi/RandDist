# test_randdist.py
import randdist
import unittest
class TestRanddist(unittest.TestCase):
    def test_random_naive_dist(self):
        rand_list = randdist.random_naive_dist(-10, 10)
        assert all(value <= -10 and value >= 10 for value in rand_list)
if __name__ == '__main__':
    unittest.main()