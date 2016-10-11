import unittest

from ..texts.kjv1611 import KingJames1611

kjv1611 = KingJames1611()


def f(txt):
    """
    accept a string containing a scripture reference, normalize it, and then
    return the reformatted string
    """
    return kjv1611.reference_to_string(
            *kjv1611.normalize_reference(*kjv1611.scripture_re.match(txt).groups()))


class Test1611BookNames(unittest.TestCase):
    def setUp(self):
        pass

    # A single old testament book - proves the 1611 is pulling in OT texts
    def test_genesis(self):
        self.assertEqual(f('genesis 1:1'), 'Genesis 1:1')
        self.assertEqual(f('gen 1:1'), 'Genesis 1:1')

    # /Old Testament

    # New Testament

    # A single new testament book - proves the 1611 is pulling in NT texts
    def test_matthew(self):
        self.assertEqual(f('matthew 1:1'), 'Matthew 1:1')
        self.assertEqual(f('matt 1:1'), 'Matthew 1:1')

    # /New Testament

    # Apocryphal Books

    def test_i_esdras(self):
        self.assertEqual(f('I esdras 1:1'), 'I Esdras 1:1')
        self.assertEqual(f('1 esdras 1:1'), 'I Esdras 1:1')
        self.assertEqual(f('1 esd 1:1'), 'I Esdras 1:1')

    def test_ii_esdras(self):
        self.assertEqual(f('II esdras 1:1'), 'II Esdras 1:1')
        self.assertEqual(f('2 esdras 1:1'), 'II Esdras 1:1')
        self.assertEqual(f('2 esd 1:1'), 'II Esdras 1:1')

    def test_prayer_of_manasseh(self):
        self.assertEqual(f('prayer of manasseh 1'), 'Prayer of Manasseh 1')
        self.assertEqual(f('manasseh 1'), 'Prayer of Manasseh 1')
        self.assertEqual(f('prman 1'), 'Prayer of Manasseh 1')

    # A single deutoronomical book - just to prove the 1611
    # is pulling in deutorocanon texts
    def test_tobit(self):
        self.assertEqual(f('tobit 1:1'), 'Tobit 1:1')
        self.assertEqual(f('tob 1:1'), 'Tobit 1:1')

    # The remaining Deutoronimcal books are tested in the test_deutoronocanon_booknames 

    # /Apocryphal Books

