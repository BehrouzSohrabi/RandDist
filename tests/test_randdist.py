import randdist
import unittest

class TestRanddist(unittest.TestCase):
    def test_randint_length_list(self):
        rand_list = randdist.randint(1, 10, seeds = 100)
        assert len(rand_list) == 100

    def test_randfloat_length_list(self):
        rand_list = randdist.randfloat(1, 10, seeds = 100)
        assert len(rand_list) == 100

    def test_randint_sample(self):
        sample = randdist.randint(1, 10, seeds = 1)
        assert type(sample) == int

    def test_randfloat_sample(self):
        sample = randdist.randfloat(1, 10, seeds = 1)
        assert type(sample) == float
    
    def test_randint_values(self):
        rand_list = randdist.randint(1, 10, seeds = 100)
        assert len(rand_list) == 100

    def test_randfloat_values(self):
        rand_list = randdist.randfloat(1, 10)
        assert len(rand_list) == 100