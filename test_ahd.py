#!/usr/bin/env python

import unittest
from test.test_support import run_unittest

from ahd import AmericanHeritage

test_dict = AmericanHeritage()


class AmericanHeritageDictionaryTestCase(unittest.TestCase):

    def setUp(self):
        self.dict = test_dict

    def assert_matched_count(self, count, results):
        self.assertEqual(count, len(results))

    def test_find_none(self):
        self.assert_matched_count(0, self.dict.lookup("nonexistent"))

    def test_find_by_exact_single(self):
        self.assert_matched_count(1, self.dict.lookup("hello"))

    def test_find_by_exact_many(self):
        self.assert_matched_count(4, self.dict.lookup("sound"))

    def test_find_by_prefix_none(self):
        self.assert_matched_count(0, self.dict.lookup_by_prefix("kneex"))

    def test_find_by_prefix_single(self):
        self.assert_matched_count(1, self.dict.lookup_by_prefix("hello"))

    def test_find_by_prefix_many(self):
        self.assert_matched_count(14, self.dict.lookup_by_prefix("knee"))

    def test_find_by_suffix_none(self):
        self.assert_matched_count(0, self.dict.lookup_by_suffix("kneex"))

    def test_find_by_suffix_single(self):
        self.assert_matched_count(1, self.dict.lookup_by_suffix("hello"))

    def test_find_by_suffix_many(self):
        self.assert_matched_count(8, self.dict.lookup_by_suffix("sound"))

    def test_find_by_fragment_none(self):
        self.assert_matched_count(0, self.dict.lookup_by_fragment("kneex"))

    def test_find_by_fragment_single(self):
        self.assert_matched_count(1, self.dict.lookup_by_fragment("vanguard"))

    def test_find_by_fragment_many(self):
        self.assert_matched_count(3, self.dict.lookup_by_fragment("hello"))


def test_main():
    run_unittest(AmericanHeritageDictionaryTestCase)

if __name__ == '__main__':
    test_main()