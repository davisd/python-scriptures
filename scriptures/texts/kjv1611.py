from __future__ import unicode_literals
from .base import Text
from .protestant import ProtestantCanon
from .deuterocanon import Deuterocanon

class KingJames1611(Text):
    """
    King James 1611 - Contains what is considered the protestant canonical texts,
    plus the Deuteronomical books (in its Apocrypha)
    plus its additional Apocryphal books (I and II Esdras)
    """
    books = ProtestantCanon.books + Deuterocanon.books + [
	('I Esdras', '1Esd', '(?:(?:1|I)(?:\s)?)Esd(?:ras)?', [58,30,24,63,73,34,15,96,55,]),
	('II Esdras', '2Esd', '(?:(?:2|II)(?:\s)?)Esd(?:ras)?', [40,48,36,52,56,59,70,63,47,59,46,51,58,48,63,78,]),
    ]

