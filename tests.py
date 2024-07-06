import unittest
from func import *


class FuncTest(unittest.TestCase):
    def test_msg_split(self):
        # given a word without space characters,
        # returns a list only containing that word
        self.assertEqual(["foo"], msg_split("foo"))

        # given a word with trailing space characters,
        # returns a list only containing that word with no space characters
        self.assertEqual(["foo"], msg_split("foo     "))

        # given two words separated by a space,
        # returns a list of those two words with no space in either word
        self.assertEqual(["$", "foo"], msg_split("$ foo"))

        # given two words separated by multiple space characters,
        # returns a list of those two words with no space in either word
        self.assertEqual(["$", "foo"], msg_split("$        foo"))

        # given two words wrapped in double quotation marks,
        # returns a list containing those two words as a single entry
        self.assertEqual(["foo", "two words", "bar"],
                         msg_split('foo "two words" bar'))

        # given a string with an unmatched double quotation mark with text
        # following it,
        # returns a list containing all text after the unmatched quote as a
        # single entry
        self.assertEqual(["two words", "three more words"],
                         msg_split('"two words" "three more words'))


if __name__ == '__main__':
    unittest.main()
