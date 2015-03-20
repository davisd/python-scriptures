import unittest

from scriptures import normalize_reference, scripture_re, reference_to_string

def f(txt):
    """
    accept a string containing a scripture reference, normalize it, and then
    return the reformatted string
    """
    return reference_to_string(
            *normalize_reference(*scripture_re.match(txt).groups()))

class TestFormatting(unittest.TestCase):
    def setUp(self):
        pass

    def test_single_reference(self):
        """
        format: book c:v
        """
        # multi-chapter book
        self.assertEqual(f('John 1:1'), 'John 1:1')
        self.assertEqual(f('John 2:3'), 'John 2:3')

        # single-chapter book
        self.assertEqual(f('Jude 1:3'), 'Jude 1:3')

    def test_single_chapter_ref(self):
        """
        format: book c

        This format is repeated in a different test for a single-chapter
        book, where it is interpreted as: book v

        """
        # multi-chapter book
        self.assertEqual(f('John 1'), 'John 1')
        self.assertEqual(f('John 2'), 'John 2')

        # N/A for single-chapter book

    def test_multiverse_ref(self):
        """
        format: book c:v-ev
        """
        # multi-chapter book
        self.assertEqual(f('John 1:1-3'), 'John 1:1-3')
        self.assertEqual(f('John 2:3-5'), 'John 2:3-5')

        # single-chapter book
        self.assertEqual(f('Jude 1:3-5'), 'Jude 1:3-5')

    def test_multichapter_multiverse_ref(self):
        """
        format: book c:v-ec:ev
        """
        # multi-chapter book
        self.assertEqual(f('John 2:2-2:7'), 'John 2:2-2:7')
        self.assertEqual(f('John 2:3-4:5'), 'John 2:3-4:5')

        # N/A for single-chapter book

    def test_multichapter_ref(self):
        """
        format: book c-ec

        This format is repeated in a different test for a single-chapter
        book, where it is interpreted as: book v-ev
        """
        # multi-chapter book
        self.assertEqual(f('John 1-5'), 'John 1-5')
        self.assertEqual(f('John 2-6'), 'John 2-6')

        # N/A for single-chapter book

    def test_singlechapter_book_verse_ref(self):
        """
        format: book v

        This format is repeated in a different test for a multi-chapter
        book, where it is interpreted as: book c
        """
        # N/A for multi-chapter book

        # single-chapter book
        self.assertEqual(f('Jude 5'), 'Jude 5')


    def test_singlechapter_book_multiverse_ref(self):
        """
        format: book v-ev

        This format is repeated in a different test for a multi-chapter
        book, where it is interpreted as: book c-ec
        """
        # N/A for multi-chapter book

        # single-chapter book
        self.assertEqual(f('Jude 2-6'), 'Jude 2-6')

