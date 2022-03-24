from vowel_count import get_count
import unittest


class TestStringMethods(unittest.TestCase):

    # @test.it("Should count all vowels")
    def test_all_vowels(self):
        self.assertEqual(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")

    # @test.it("Should not count \"y\"")
    def test_only_yfdg(self):
        self.assertEqual(get_count("y"), 0, f"Incorrect answer for \"y\"")

    # @test.it("Should return 0 when no vowels")
    def test_no_vowelssgf(self):
        self.assertEqual(get_count("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")

    # @test.it("Should return 0 for empty string")
    def test_abracadabra(self):
        self.assertEqual(get_count("abracadabra"), 5, f"Incorrect answer for empty string")

    # @test.it("Should return 5 for \"abracadabra\"")
    def test_no_vowels(self):
        self.assertEqual(get_count(""), 0, f"Incorrect answer for \"abracadabra\"")

