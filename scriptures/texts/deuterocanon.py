from __future__ import unicode_literals
from .base import Text


class Deuterocanon(Text):
    """
    Deuterocanonical Books
    """
    books = {
        'tob': ('Tobit', 'Tob', 'Tob(?:it)?',
                [22, 14, 17, 21, 22, 17, 18, 21, 6, 12, 19, 22, 18, 15]),

        'jdt': ('Judith', 'Jdt', 'Jud(?:ith)?',
                [
                    16, 28, 10, 15, 24, 21, 32, 35, 14,
                    23, 23, 20, 20, 19, 13, 25
                ]),

        'addesth': ('Additions to Esther', 'AddEsth',
            '(?:AddEsth|(?:Additions to|Rest of) Esther|Esther \\(Greek\\))',
                    [
                        39, 23, 22, 47, 28, 14, 10, 41, 32, 13
                    ]),

        'wis': ('The Wisdom of Solomon', 'Wis',
                '(?:The )?Wis(?:dom(?: of Solomon)?)?',
                [
                    16, 24, 19, 20, 23, 25, 30, 20, 18,
                    21, 26, 27, 19, 31, 19, 29, 21,
                    25, 22
                ]),

        'sir': ('Sirach', 'Sir',
            'Sir(?:ach)?|Ecclesiasticus',
                [
                    30, 18, 31, 31, 15, 37, 36, 19, 18,
                    31, 34, 18, 26, 27, 20, 30, 32, 33,
                    30, 31, 28, 27, 34, 26, 29, 30,
                    26, 28, 25, 31, 24, 31, 26, 20,
                    26, 31, 34, 35, 30, 23, 25, 33,
                    23, 26, 20, 25, 25, 16, 29, 30
                ]),

        'bar': ('Baruch', 'Bar', 'Bar(?:uch)?',
                [
                    21, 35, 37, 37, 9
                ]),

        'epjer': ('Letter of Jeremiah', 'EpJer',
            'EpJer|Letter of Jeremiah',
                [73]),

        'prazar': ('Prayer of Azariah', 'prazar',
            '(?:prayer of |Pr)?Azar(?:iah)?|Song of (?:the )?Three Children',
                        [68]),

        'sus': ('Susanna', 'susanna',
            '(?:Story of )?sus(?:anna)?', 
                [64]),
        
        'bel': ('Bel and the Dragon', 'bel',
                      'bel(?:(?: and the)? dragon)?',
                      [42]),

        '1macc': ('I Maccabees', '1Macc', '(?:1|I) ?Macc(?:abees)?',
                  [
                      64, 70, 60, 61, 68, 63, 50, 32, 73,
                      89, 74, 53, 53, 49, 41, 24
                  ]),

        '2macc': ('II Maccabees', '2Macc', '(?:2|II) ?Macc(?:abees)?',
                  [
                      36, 32, 40, 50, 27, 31, 42, 36, 29,
                      38, 38, 45, 26, 46, 39
                  ]),
    }
