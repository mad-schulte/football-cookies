#!/usr/bin/env python

import unittest
from histogram import *

# tests have to go avove the call to unittest
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_strip_lower(self):
        start = "TEST    test "
        result = strip_and_lower(start)
        self.assertEqual(result, "testtest")

    def test_letter_required_later_null(self):
        self.assertEqual(letter_required_later({}, ' '), None)

    def test_letter_required_later_true(self):
        self.assertEqual(letter_required_later({'t':3}, 't'), True)

    def test_find_nonrequired_letter_not_found(self):
        self.assertEqual(find_nonrequired_letter({'t':3}, 'y'), 'y')

    def test_find_nonrequired_letter_found(self):
        self.assertEqual(find_nonrequired_letter({'t':3}, 't'), "NONE")

    def test_add_to_needed_later_empty(self):
        test_dict = {}
        add_to_needed_later({}, '')
        self.assertEqual(test_dict, {})

    def test_add_to_needed_later_upper(self):
        test_dict = {}
        add_to_needed_later(test_dict, 'A')
        self.assertEqual(test_dict, {'a':1})

    def test_add_to_needed_later_already(self):
        test_dict = {'a':1}
        add_to_needed_later(test_dict, 'a')
        self.assertEqual(test_dict, {'a':2})


if __name__ == '__main__':

    unittest.main()
