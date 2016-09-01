import unittest

from .. import normalize_reference, scripture_re, reference_to_string

def f(txt):
    """
    accept a string containing a scripture reference, normalize it, and then
    return the reformatted string
    """
    return reference_to_string(
            *normalize_reference(*scripture_re.match(txt).groups()))

class TestReferenceToSting(unittest.TestCase):
    def setUp(self):
        pass

    def test_single_reference(self):
        """
        for multi-chapter books, output should be
          book c:v
        for single-chapter books, output should be
          book v

        """
        # multi-chapter book
        self.assertEqual(f('John 1:1'), 'John 1:1')
        self.assertEqual(f('John 2:3'), 'John 2:3')

        # single-chapter book
        self.assertEqual(f('Jude 3'), 'Jude 3')
        self.assertEqual(f('Jude 1:3'), 'Jude 3')

    def test_single_chapter_ref(self):
        """
        for multi-chapter books, output should be
          book c
        for single-chapter books, this does not make sense, as b x is
        interpreted as b v

        """
        # multi-chapter book
        self.assertEqual(f('John 1:1-51'), 'John 1')
        self.assertEqual(f('John 1'), 'John 1')
        self.assertEqual(f('John 2:1-25'), 'John 2')
        self.assertEqual(f('John 2'), 'John 2')

    def test_multiverse_ref(self):
        """
        for multi-chapter books, output should be
          book c:v-ev
        for single-chapter books, output should be
          book v-ev
        """
        # multi-chapter book
        self.assertEqual(f('John 1:1-3'), 'John 1:1-3')
        self.assertEqual(f('John 2:3-5'), 'John 2:3-5')

        # single-chapter book
        self.assertEqual(f('Jude 1:3-5'), 'Jude 3-5')
        self.assertEqual(f('Jude 3-5'), 'Jude 3-5')

    def test_multichapter_multiverse_ref(self):
        """
        for multi-chapter books, output should be
          b c:v-ec:ev
        for single-chapter books, input and output chapters are both one
          b v-ev
        """
        # multi-chapter book
        self.assertEqual(f('John 2:3-4:5'), 'John 2:3-4:5')

        # single-chapter book
        self.assertEqual(f('Jude 1:3-1:5'), 'Jude 3-5')

    def test_multichapter_ref(self):
        """
        for multi-chapter books, output should be:
          b c-ec
        for single-chapter books, this does not make sense, as b x-x is
        interpreted as b v-ev
        """
        # multi-chapter book
        self.assertEqual(f('John 1-5'), 'John 1-5')
        self.assertEqual(f('John 2-6'), 'John 2-6')

        # N/A for single-chapter book

    def test_singlechapter_book_verse_ref(self):
        """
        for multi-chapter books, this does not make sense as b x is interpreted
        as book c

        for single-chapter books, output should be:
          b v
        """
        # N/A for multi-chapter book

        # single-chapter book
        self.assertEqual(f('Jude 5'), 'Jude 5')


    def test_singlechapter_book_multiverse_ref(self):
        """
        for mult-chapter books, this does not make sense as b x-x is
        interpreted as b c-ec

        for single-chapter books, output should be:
          b v-ev
        """
        # N/A for multi-chapter book

        # single-chapter book
        self.assertEqual(f('Jude 2-6'), 'Jude 2-6')

    def test_implied_first_verse_ref(self):
        """
        for multi-chapter books, single chapter ref, output should be
          b c:v-ev
        for multi-chapter books, multi chapter ref, output should be
          b c:v-ec:ev
        for single-chapter books, input and output chapters are both one
          b v-ev
        """

        # multi-chapter book
        self.assertEqual(f('John 2-2:4'), 'John 2:1-4')
        self.assertEqual(f('John 2-3:3'), 'John 2:1-3:3')

        # single-chapter book
        self.assertEqual(f('Jude 1-1:6'), 'Jude 1-6')
