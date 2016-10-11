from __future__ import unicode_literals
from .base import Text
from .protestant import ProtestantCanon
from .deuterocanon import Deuterocanon


class KingJames1611(Text):
    """
    KingJames1611 - Contains what is considered the protestant canonical texts,
    plus the Deuteronomical books (in its Apocrypha)
    plus its additional Apocryphal books (I and II Esdras)
    """
    books = {}
    books.update(ProtestantCanon.books)
    books.update(Deuterocanon.books)
    books.update({
        '1esd': ('I Esdras', '1Esd', '(?:(?:1|I)(?:\s)?)Esd(?:ras)?',
                 [58, 30, 24, 63, 73, 34, 15, 96, 55]),
        '2esd': ('II Esdras', '2Esd', '(?:(?:2|II)(?:\s)?)Esd(?:ras)?',
                 [40, 48, 36, 52, 56, 59, 70, 63,
                  47, 59, 46, 51, 58, 48, 63, 78]),
        'prman': ('Prayer of Manasseh', 'prman',
                  'prman|(?:prayer of )?manasseh',
                  [15]),
    })

