from unittest import TestCase

from prime_factor import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor_of_1(self):
        self.assertEqual(PrimeFactor.of(1), [])

    def test_prime_factor_of_2(self):
        self.assertEqual(PrimeFactor.of(2), [2])
