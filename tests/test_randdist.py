import randdist
import unittest

class TestRanddist(unittest.TestCase):
    def test_randint(self):
        rand_list, rand_sample = randdist.randint(1, 10)
        assert len(rand_list) > 0 and rand_sample >=1 and rand_sample <= 10

    def test_randfloat(self):
        rand_list, rand_sample = randdist.randfloat(1, 10)
        assert len(rand_list) > 0 and rand_sample >=1 and rand_sample <= 10