from unittest import TestCase


class TestLongest_common_substr(TestCase):
    def test_longest_common_substr(self):
        try:
            from build import longest_common_substr
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, longest_common_substr, None, None)
        self.assertEqual(longest_common_substr('', ''), '')
        str0 = 'ABCDEFGHIJ'
        str1 = 'FOOBCDBCDE'
        expected = 'BCDE'
        self.assertEqual(longest_common_substr(str0, str1), expected)
