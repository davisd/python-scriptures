import unittest

from .. import normalize_reference, scripture_re, reference_to_string

def f(txt):
    """
    accept a string containing a scripture reference, normalize it, and then
    return the reformatted string
    """
    return reference_to_string(
            *normalize_reference(*scripture_re.match(txt).groups()))

class TestBookNames(unittest.TestCase):
    def setUp(self):
        pass

    # Old Testament

    def test_genesis(self):
        self.assertEqual(f('genesis 1:1'), 'Genesis 1:1')
        self.assertEqual(f('gen 1:1'), 'Genesis 1:1')

    def test_exodus(self):
        self.assertEqual(f('exodus 1:1'), 'Exodus 1:1')
        self.assertEqual(f('exod 1:1'), 'Exodus 1:1')

    def test_leviticus(self):
        self.assertEqual(f('leviticus 1:1'), 'Leviticus 1:1')
        self.assertEqual(f('lev 1:1'), 'Leviticus 1:1')

    def test_numbers(self):
        self.assertEqual(f('numbers 1:1'), 'Numbers 1:1')
        self.assertEqual(f('num 1:1'), 'Numbers 1:1')

    def test_deuteronomy(self):
        self.assertEqual(f('deuteronomy 1:1'), 'Deuteronomy 1:1')
        self.assertEqual(f('deut 1:1'), 'Deuteronomy 1:1')

    def test_joshua(self):
        self.assertEqual(f('joshua 1:1'), 'Joshua 1:1')
        self.assertEqual(f('josh 1:1'), 'Joshua 1:1')

    def test_judges(self):
        self.assertEqual(f('judges 1:1'), 'Judges 1:1')
        self.assertEqual(f('judg 1:1'), 'Judges 1:1')

    def test_ruth(self):
        self.assertEqual(f('ruth 1:1'), 'Ruth 1:1')

    def test_i_samuel(self):
        self.assertEqual(f('I samuel 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('1 samuel 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('I sam 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('1 sam 1:1'), 'I Samuel 1:1')
        self.assertEqual(f('1sam 1:1'), 'I Samuel 1:1')

    def test_ii_samuel(self):
        self.assertEqual(f('II samuel 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('2 samuel 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('II sam 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('2 sam 1:1'), 'II Samuel 1:1')
        self.assertEqual(f('2sam 1:1'), 'II Samuel 1:1')

    def test_i_kings(self):
        self.assertEqual(f('I kings 1:1'), 'I Kings 1:1')
        self.assertEqual(f('1 kings 1:1'), 'I Kings 1:1')
        self.assertEqual(f('I kgs 1:1'), 'I Kings 1:1')
        self.assertEqual(f('1 kgs 1:1'), 'I Kings 1:1')
        self.assertEqual(f('1kgs 1:1'), 'I Kings 1:1')

    def test_ii_kings(self):
        self.assertEqual(f('II kings 1:1'), 'II Kings 1:1')
        self.assertEqual(f('2 kings 1:1'), 'II Kings 1:1')
        self.assertEqual(f('II kgs 1:1'), 'II Kings 1:1')
        self.assertEqual(f('2 kgs 1:1'), 'II Kings 1:1')
        self.assertEqual(f('2kgs 1:1'), 'II Kings 1:1')

    def test_i_chronicles(self):
        self.assertEqual(f('I chronicles 1:1'), 'I Chronicles 1:1')
        self.assertEqual(f('1 chronicles 1:1'), 'I Chronicles 1:1')

        self.assertEqual(f('I chr 1:1'), 'I Chronicles 1:1')
        self.assertEqual(f('I chro 1:1'), 'I Chronicles 1:1')
        self.assertEqual(f('I chron 1:1'), 'I Chronicles 1:1')

        self.assertEqual(f('1 chr 1:1'), 'I Chronicles 1:1')
        self.assertEqual(f('1 chro 1:1'), 'I Chronicles 1:1')
        self.assertEqual(f('1 chron 1:1'), 'I Chronicles 1:1')

    def test_ii_chronicles(self):
        self.assertEqual(f('II chronicles 1:1'), 'II Chronicles 1:1')
        self.assertEqual(f('2 chronicles 1:1'), 'II Chronicles 1:1')

        self.assertEqual(f('II chr 1:1'), 'II Chronicles 1:1')
        self.assertEqual(f('II chro 1:1'), 'II Chronicles 1:1')
        self.assertEqual(f('II chron 1:1'), 'II Chronicles 1:1')

        self.assertEqual(f('2 chr 1:1'), 'II Chronicles 1:1')
        self.assertEqual(f('2 chro 1:1'), 'II Chronicles 1:1')
        self.assertEqual(f('2 chron 1:1'), 'II Chronicles 1:1')


    def test_ezra(self):
        self.assertEqual(f('ezra 1:1'), 'Ezra 1:1')

    def test_nehemiah(self):
        self.assertEqual(f('nehemiah 1:1'), 'Nehemiah 1:1')
        self.assertEqual(f('neh 1:1'), 'Nehemiah 1:1')

    def test_esther(self):
        self.assertEqual(f('esther 1:1'), 'Esther 1:1')
        self.assertEqual(f('esth 1:1'), 'Esther 1:1')

    def test_job(self):
        self.assertEqual(f('job 1:1'), 'Job 1:1')

    def test_psalms(self):
        self.assertEqual(f('psalms 1:1'), 'Psalms 1:1')
        self.assertEqual(f('ps 1:1'), 'Psalms 1:1')
        self.assertEqual(f('psa 1:1'), 'Psalms 1:1')
        self.assertEqual(f('psalm 1:1'), 'Psalms 1:1')

    def test_proverbs(self):
        self.assertEqual(f('proverbs 1:1'), 'Proverbs 1:1')
        self.assertEqual(f('prov 1:1'), 'Proverbs 1:1')

    def test_ecclesiastes(self):
        self.assertEqual(f('ecclesiastes 1:1'), 'Ecclesiastes 1:1')
        self.assertEqual(f('ecc 1:1'), 'Ecclesiastes 1:1')
        self.assertEqual(f('eccl 1:1'), 'Ecclesiastes 1:1')
        self.assertEqual(f('eccles 1:1'), 'Ecclesiastes 1:1')

    def test_song_of_solomon(self):
        self.assertEqual(f('song of solomon 1:1'), 'Song of Solomon 1:1')
        self.assertEqual(f('song 1:1'), 'Song of Solomon 1:1')
        self.assertEqual(f('song of sol 1:1'), 'Song of Solomon 1:1')

    def test_isaiah(self):
        self.assertEqual(f('isaiah 1:1'), 'Isaiah 1:1')
        self.assertEqual(f('isa 1:1'), 'Isaiah 1:1')

    def test_jeremiah(self):
        self.assertEqual(f('jeremiah 1:1'), 'Jeremiah 1:1')
        self.assertEqual(f('jer 1:1'), 'Jeremiah 1:1')

    def test_lamentations(self):
        self.assertEqual(f('lamentations 1:1'), 'Lamentations 1:1')
        self.assertEqual(f('lam 1:1'), 'Lamentations 1:1')

    def test_ezekiel(self):
        self.assertEqual(f('ezekiel 1:1'), 'Ezekiel 1:1')
        self.assertEqual(f('ezek 1:1'), 'Ezekiel 1:1')

    def test_daniel(self):
        self.assertEqual(f('daniel 1:1'), 'Daniel 1:1')
        self.assertEqual(f('dan 1:1'), 'Daniel 1:1')

    def test_hosea(self):
        self.assertEqual(f('hosea 1:1'), 'Hosea 1:1')
        self.assertEqual(f('hos 1:1'), 'Hosea 1:1')

    def test_joel(self):
        self.assertEqual(f('joel 1:1'), 'Joel 1:1')

    def test_amos(self):
        self.assertEqual(f('amos 1:1'), 'Amos 1:1')

    def test_obadiah(self):
        self.assertEqual(f('obadiah 1:1'), 'Obadiah 1')
        self.assertEqual(f('obad 1:1'), 'Obadiah 1')

    def test_jonah(self):
        self.assertEqual(f('jonah 1:1'), 'Jonah 1:1')
        self.assertEqual(f('jon 1:1'), 'Jonah 1:1')

    def test_micah(self):
        self.assertEqual(f('micah 1:1'), 'Micah 1:1')
        self.assertEqual(f('mic 1:1'), 'Micah 1:1')

    def test_nahum(self):
        self.assertEqual(f('nahum 1:1'), 'Nahum 1:1')
        self.assertEqual(f('nah 1:1'), 'Nahum 1:1')

    def test_habakkuk(self):
        self.assertEqual(f('habakkuk 1:1'), 'Habakkuk 1:1')
        self.assertEqual(f('hab 1:1'), 'Habakkuk 1:1')

    def test_zephaniah(self):
        self.assertEqual(f('zephaniah 1:1'), 'Zephaniah 1:1')
        self.assertEqual(f('zeph 1:1'), 'Zephaniah 1:1')

    def test_haggai(self):
        self.assertEqual(f('haggai 1:1'), 'Haggai 1:1')
        self.assertEqual(f('hag 1:1'), 'Haggai 1:1')

    def test_zechariah(self):
        self.assertEqual(f('zechariah 1:1'), 'Zechariah 1:1')
        self.assertEqual(f('zech 1:1'), 'Zechariah 1:1')

    def test_malachi(self):
        self.assertEqual(f('malachi 1:1'), 'Malachi 1:1')
        self.assertEqual(f('mal 1:1'), 'Malachi 1:1')

    # /Old Testament

    # New Testament

    def test_matthew(self):
        self.assertEqual(f('matthew 1:1'), 'Matthew 1:1')
        self.assertEqual(f('matt 1:1'), 'Matthew 1:1')

    def test_mark(self):
        self.assertEqual(f('mark 1:1'), 'Mark 1:1')

    def test_luke(self):
        self.assertEqual(f('luke 1:1'), 'Luke 1:1')

    def test_john(self):
        self.assertEqual(f('john 1:1'), 'John 1:1')

    def test_acts(self):
        self.assertEqual(f('acts 1:1'), 'Acts 1:1')

    def test_romans(self):
        self.assertEqual(f('romans 1:1'), 'Romans 1:1')
        self.assertEqual(f('rom 1:1'), 'Romans 1:1')

    def test_i_corinthians(self):
        self.assertEqual(f('I corinthians 1:1'), 'I Corinthians 1:1')
        self.assertEqual(f('I cor 1:1'), 'I Corinthians 1:1')
        self.assertEqual(f('1 corinthians 1:1'), 'I Corinthians 1:1')
        self.assertEqual(f('1 cor 1:1'), 'I Corinthians 1:1')

        self.assertEqual(f('Icorinthians 1:1'), 'I Corinthians 1:1')
        self.assertEqual(f('Icor 1:1'), 'I Corinthians 1:1')
        self.assertEqual(f('1corinthians 1:1'), 'I Corinthians 1:1')
        self.assertEqual(f('1cor 1:1'), 'I Corinthians 1:1')

    def test_ii_corinthians(self):
        self.assertEqual(f('II corinthians 1:1'), 'II Corinthians 1:1')
        self.assertEqual(f('II cor 1:1'), 'II Corinthians 1:1')
        self.assertEqual(f('2 corinthians 1:1'), 'II Corinthians 1:1')
        self.assertEqual(f('2 cor 1:1'), 'II Corinthians 1:1')

        self.assertEqual(f('IIcorinthians 1:1'), 'II Corinthians 1:1')
        self.assertEqual(f('IIcor 1:1'), 'II Corinthians 1:1')
        self.assertEqual(f('2corinthians 1:1'), 'II Corinthians 1:1')
        self.assertEqual(f('2cor 1:1'), 'II Corinthians 1:1')

    def test_galatians(self):
        self.assertEqual(f('galatians 1:1'), 'Galatians 1:1')
        self.assertEqual(f('gal 1:1'), 'Galatians 1:1')

    def test_ephesians(self):
        self.assertEqual(f('ephesians 1:1'), 'Ephesians 1:1')
        self.assertEqual(f('eph 1:1'), 'Ephesians 1:1')

    def test_philippians(self):
        self.assertEqual(f('philippians 1:1'), 'Philippians 1:1')
        self.assertEqual(f('phil 1:1'), 'Philippians 1:1')

    def test_colossians(self):
        self.assertEqual(f('colossians 1:1'), 'Colossians 1:1')
        self.assertEqual(f('col 1:1'), 'Colossians 1:1')

    def test_i_thessalonians(self):
        self.assertEqual(f('I thessalonians 1:1'), 'I Thessalonians 1:1')
        self.assertEqual(f('I thess 1:1'), 'I Thessalonians 1:1')
        self.assertEqual(f('1 thessalonians 1:1'), 'I Thessalonians 1:1')
        self.assertEqual(f('1 thess 1:1'), 'I Thessalonians 1:1')

        self.assertEqual(f('Ithessalonians 1:1'), 'I Thessalonians 1:1')
        self.assertEqual(f('Ithess 1:1'), 'I Thessalonians 1:1')
        self.assertEqual(f('1thessalonians 1:1'), 'I Thessalonians 1:1')
        self.assertEqual(f('1thess 1:1'), 'I Thessalonians 1:1')

    def test_ii_thessalonians(self):
        self.assertEqual(f('II thessalonians 1:1'), 'II Thessalonians 1:1')
        self.assertEqual(f('II thess 1:1'), 'II Thessalonians 1:1')
        self.assertEqual(f('2 thessalonians 1:1'), 'II Thessalonians 1:1')
        self.assertEqual(f('2 thess 1:1'), 'II Thessalonians 1:1')

        self.assertEqual(f('IIthessalonians 1:1'), 'II Thessalonians 1:1')
        self.assertEqual(f('IIthess 1:1'), 'II Thessalonians 1:1')
        self.assertEqual(f('2thessalonians 1:1'), 'II Thessalonians 1:1')
        self.assertEqual(f('2thess 1:1'), 'II Thessalonians 1:1')


    def test_i_timothy(self):
        self.assertEqual(f('I timothy 1:1'), 'I Timothy 1:1')
        self.assertEqual(f('I tim 1:1'), 'I Timothy 1:1')
        self.assertEqual(f('1 timothy 1:1'), 'I Timothy 1:1')
        self.assertEqual(f('1 tim 1:1'), 'I Timothy 1:1')

        self.assertEqual(f('Itimothy 1:1'), 'I Timothy 1:1')
        self.assertEqual(f('Itim 1:1'), 'I Timothy 1:1')
        self.assertEqual(f('1timothy 1:1'), 'I Timothy 1:1')
        self.assertEqual(f('1tim 1:1'), 'I Timothy 1:1')

    def test_ii_timothy(self):
        self.assertEqual(f('II timothy 1:1'), 'II Timothy 1:1')
        self.assertEqual(f('II tim 1:1'), 'II Timothy 1:1')
        self.assertEqual(f('2 timothy 1:1'), 'II Timothy 1:1')
        self.assertEqual(f('2 tim 1:1'), 'II Timothy 1:1')

        self.assertEqual(f('IItimothy 1:1'), 'II Timothy 1:1')
        self.assertEqual(f('IItim 1:1'), 'II Timothy 1:1')
        self.assertEqual(f('2timothy 1:1'), 'II Timothy 1:1')
        self.assertEqual(f('2tim 1:1'), 'II Timothy 1:1')

    def test_titus(self):
        self.assertEqual(f('titus 1:1'), 'Titus 1:1')
        self.assertEqual(f('tit 1:1'), 'Titus 1:1')

    def test_philemon(self):
        self.assertEqual(f('philemon 1:1'), 'Philemon 1')
        self.assertEqual(f('phile 1:1'), 'Philemon 1')
        self.assertEqual(f('philem 1:1'), 'Philemon 1')
        self.assertEqual(f('phlm 1:1'), 'Philemon 1')

    def test_hebrews(self):
        self.assertEqual(f('hebrews 1:1'), 'Hebrews 1:1')
        self.assertEqual(f('heb 1:1'), 'Hebrews 1:1')

    def test_james(self):
        self.assertEqual(f('james 1:1'), 'James 1:1')
        self.assertEqual(f('jas 1:1'), 'James 1:1')

    def test_i_peter(self):
        self.assertEqual(f('I peter 1:1'), 'I Peter 1:1')
        self.assertEqual(f('I pet 1:1'), 'I Peter 1:1')
        self.assertEqual(f('1 peter 1:1'), 'I Peter 1:1')
        self.assertEqual(f('1 pet 1:1'), 'I Peter 1:1')

        self.assertEqual(f('Ipeter 1:1'), 'I Peter 1:1')
        self.assertEqual(f('Ipet 1:1'), 'I Peter 1:1')
        self.assertEqual(f('1peter 1:1'), 'I Peter 1:1')
        self.assertEqual(f('1pet 1:1'), 'I Peter 1:1')

    def test_i_peter(self):
        self.assertEqual(f('II peter 1:1'), 'II Peter 1:1')
        self.assertEqual(f('II pet 1:1'), 'II Peter 1:1')
        self.assertEqual(f('2 peter 1:1'), 'II Peter 1:1')
        self.assertEqual(f('2 pet 1:1'), 'II Peter 1:1')

        self.assertEqual(f('IIpeter 1:1'), 'II Peter 1:1')
        self.assertEqual(f('IIpet 1:1'), 'II Peter 1:1')
        self.assertEqual(f('2peter 1:1'), 'II Peter 1:1')
        self.assertEqual(f('2pet 1:1'), 'II Peter 1:1')


    def test_i_john(self):
        self.assertEqual(f('I john 1:1'), 'I John 1:1')
        self.assertEqual(f('1 john 1:1'), 'I John 1:1')

        self.assertEqual(f('Ijohn 1:1'), 'I John 1:1')
        self.assertEqual(f('1john 1:1'), 'I John 1:1')

    def test_ii_John(self):
        self.assertEqual(f('II john 1:1'), 'II John 1')
        self.assertEqual(f('2 john 1:1'), 'II John 1')

        self.assertEqual(f('IIjohn 1:1'), 'II John 1')
        self.assertEqual(f('2john 1:1'), 'II John 1')

    def test_iii_john(self):
        self.assertEqual(f('III john 1:1'), 'III John 1')
        self.assertEqual(f('3 john 1:1'), 'III John 1')

        self.assertEqual(f('IIIjohn 1:1'), 'III John 1')
        self.assertEqual(f('3john 1:1'), 'III John 1')

    def test_jude(self):
        self.assertEqual(f('jude 1:1'), 'Jude 1')

    def test_revelation(self):
        self.assertEqual(f('revelation 1:1'), 'Revelation of Jesus Christ 1:1')
        self.assertEqual(f('revelation of jesus christ 1:1'), 'Revelation of Jesus Christ 1:1')
        self.assertEqual(f('rev 1:1'), 'Revelation of Jesus Christ 1:1')

    # /New Testament

