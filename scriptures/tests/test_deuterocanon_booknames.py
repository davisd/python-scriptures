import unittest

from ..texts.deuterocanon import Deuterocanon

dc=Deuterocanon()

def f(txt):
    """
    accept a string containing a scripture reference, normalize it, and then
    return the reformatted string
    """
    return dc.reference_to_string(
            *dc.normalize_reference(*dc.scripture_re.match(txt).groups()))

class TestDeuterocanonBookNames(unittest.TestCase):
    def setUp(self):
        pass

    def test_tobit(self):
        self.assertEqual(f('tobit 1:1'), 'Tobit 1:1')
        self.assertEqual(f('tob 1:1'), 'Tobit 1:1')

    def test_judith(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_additions_to_esther(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_wisdom_of_solomon(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_ecclesiasticus_aka_sirach(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_baruch(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_letter_of_jeremiah(self):
        # TODO
        raise Exception('Not yet implemented')

    def testprayer_of_azariah(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_susanna(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_bel_and_the_dragon(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_prayer_of_manasseh(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_1_maccabees(self):
        # TODO
        raise Exception('Not yet implemented')

    def test_2_maccabees(self):
        # TODO
        raise Exception('Not yet implemented')

