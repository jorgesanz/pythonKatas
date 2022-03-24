from calculation_with_numbers import *
import unittest


class TestStringMethods(unittest.TestCase):

    # @test.it("Should count all vowels")
    def test_describe(self):
        self.assertEqual(35, seven(times(five())))
        self.assertEqual(13, four(plus(nine())))
        self.assertEqual(5, eight(minus(three())))
        self.assertEqual(3, six(divided_by(two())))


