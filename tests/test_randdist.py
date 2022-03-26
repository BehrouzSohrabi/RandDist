import randdist
import unittest

class TestRanddist(unittest.TestCase):
    def test_randint_length_list(self):
        rand_list = randdist.randint(1, 10, seeds = 100)
        self.assertEqual(len(rand_list), 100)

    def test_randfloat_length_list(self):
        rand_list = randdist.randfloat(1, 10, seeds = 100)
        self.assertEqual(len(rand_list), 100)

    def test_randint_sample(self):
        sample = randdist.randint(1, 10, sample_size = 1)
        self.assertTrue(isinstance(sample, int))

    def test_randfloat_sample(self):
        sample = randdist.randfloat(1, 10, sample_size = 1)
        self.assertTrue(isinstance(sample, float))