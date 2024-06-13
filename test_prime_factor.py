from unittest import TestCase

from prime_factor import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor_of_1(self):
        pf = PrimeFactor()

        expected = pf.of(1)

        self.assertIsNone(expected)
