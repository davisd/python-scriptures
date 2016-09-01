import unittest

from .. import normalize_reference, scripture_re

def normalize(txt):
    return normalize_reference(*scripture_re.match(txt).groups())

class TestNormalization(unittest.TestCase):
    def setUp(self):
        pass

    def test_single_reference(self):
        """
        format: book c:v
        """
        # multi-chapter book
        self.assertEqual(normalize('John 1:1'), ('John', 1, 1, 1, 1))
        self.assertEqual(normalize('John 2:3'), ('John', 2, 3, 2, 3))

        # single-chapter book
        self.assertEqual(normalize('Jude 1:3'), ('Jude', 1, 3, 1, 3))

    def test_single_chapter_ref(self):
        """
        format: book c

        This format is repeated in a different test for a single-chapter
        book, where it is interpreted as: book v

        """
        # multi-chapter book
        self.assertEqual(normalize('John 1'), ('John', 1, 1, 1, 51))
        self.assertEqual(normalize('John 2'), ('John', 2, 1, 2, 25))

        # N/A for single-chapter book

    def test_multiverse_ref(self):
        """
        format: book c:v-ev
        """
        # multi-chapter book
        self.assertEqual(normalize('John 1:1-3'), ('John', 1, 1, 1, 3))
        self.assertEqual(normalize('John 2:3-5'), ('John', 2, 3, 2, 5))

        # single-chapter book
        self.assertEqual(normalize('Jude 1:3-5'), ('Jude', 1, 3, 1, 5))

    def test_multichapter_multiverse_ref(self):
        """
        format: book c:v-ec:ev
        """
        # multi-chapter book
        self.assertEqual(normalize('John 2:2-2:7'), ('John', 2, 2, 2, 7))
        self.assertEqual(normalize('John 2:3-4:5'), ('John', 2, 3, 4, 5))

        # N/A for single-chapter book

    def test_multichapter_ref(self):
        """
        format: book c-ec

        This format is repeated in a different test for a single-chapter
        book, where it is interpreted as: book v-ev
        """
        # multi-chapter book
        self.assertEqual(normalize('John 1-5'), ('John', 1, 1, 5, 47))
        self.assertEqual(normalize('John 2-6'), ('John', 2, 1, 6, 71))

        # N/A for single-chapter book

    def test_singlechapter_book_verse_ref(self):
        """
        format: book v

        This format is repeated in a different test for a multi-chapter
        book, where it is interpreted as: book c
        """
        # N/A for multi-chapter book

        # single-chapter book
        self.assertEqual(normalize('Jude 5'), ('Jude', 1, 5, 1, 5))


    def test_singlechapter_book_multiverse_ref(self):
        """
        format: book v-ev

        This format is repeated in a different test for a multi-chapter
        book, where it is interpreted as: book c-ec
        """
        # N/A for multi-chapter book

        # single-chapter book
        self.assertEqual(normalize('Jude 2-6'), ('Jude', 1, 2, 1, 6))

    def test_implied_first_verse_ref_single_chapter(self):
        """
        format: book ch-ech:ev
        """
        # single-chapter book
        self.assertEqual(normalize('1 John 1-1:5'), ('I John', 1, 1, 1, 5))

        # multi-chapter book
        self.assertEqual(normalize('I Sam 28-28:2'), ('I Samuel', 28, 1, 28, 2))


    def test_implied_first_verse_ref_multi_chapter(self):
        """
        format: book ch-ech:ev
        """
        # single-chapter book
        self.assertEqual(normalize('Jude 1-1:5'), ('Jude', 1, 1, 1, 5))

        # multi-chapter book
        self.assertEqual(normalize('I Sam 1-2:15'), ('I Samuel', 1, 1, 2, 15))
        self.assertEqual(normalize('I Sam 2-3:5'), ('I Samuel', 2, 1, 3, 5))


