import re

from .bible_re import testaments, book_re, scripture_re

class InvalidReferenceException(Exception):
    """
    Invalid Reference Exception
    """
    pass

def get_book(name):
    """
    Get a book from its name or None if not found
    """
    for books in testaments.values():
        for book in books:
            if re.match('^%s$' % book[2], name, re.IGNORECASE):
                return book
    return None

def extract(text):
    """
    Extract a list of tupled scripture references from a block of text
    """
    references = []
    for r in re.finditer(scripture_re, text):
        try:
            references.append(normalize_reference(*r.groups()))
        except InvalidReferenceException:
            pass
    return references

def is_valid_reference(bookname, chapter, verse=None,
                                 end_chapter=None, end_verse=None):
    """
    Check to see if a scripture reference is valid
    """
    try:
        return normalize_reference(bookname, chapter, verse,
            end_chapter, end_verse) is not None
    except InvalidReferenceException:
        return False

def reference_to_string(bookname, chapter, verse=None,
                        end_chapter=None, end_verse=None):
    """
    Get a display friendly string from a scripture reference
    """
    book=None

    bn, c, v, ec, ev = normalize_reference(bookname, chapter, verse,
        end_chapter, end_verse)

    book = get_book(bn)

    if c == ec and len(book[3]) == 1: # single chapter book
        if v == ev: # single verse
            return '{0} {1}'.format(bn, v)
        else: # multiple verses
            return '{0} {1}-{2}'.format(bn, v, ev)
    else: # multichapter book
        if c == ec: # same start and end chapters
            if v == 1 and ev == book[3][c-1]: # full chapter
                return '{0} {1}'.format(bn, c)
            elif v == ev: # single verse
                return '{0} {1}:{2}'.format(bn, c, v)
            else: # multiple verses
                return '{0} {1}:{2}-{3}'.format(
                    bn, c, v, ev)
        else: # multiple chapters
            if v == 1 and ev == book[3][ec-1]: # multichapter ref
                return '{0} {1}-{2}'.format(bn, c, ec)
            else: # multi-chapter, multi-verse ref
                return '{0} {1}:{2}-{3}:{4}'.format(bn, c, v, ec, ev)

def normalize_reference(bookname, chapter, verse=None,
                                  end_chapter=None, end_verse=None):
    """
    Get a complete five value tuple scripture reference with full book name
    from partial data
    """
    book = get_book(bookname)

    # SPECIAL CASES FOR: BOOKS WITH ONE CHAPTER AND MULTI-CHAPTER REFERENCES

    # If the ref is in format: (Book, #, None, None, ?)
    # This is a special case and indicates a reference in the format: Book 2-3
    if chapter is not None and verse is None and end_chapter is None:
        # If there is only one chapter in this book, set the chapter to one and
        # treat the incoming chapter argument as though it were the verse.
        # This normalizes references such as:
        # Jude 2 and Jude 2-4
        if len(book[3]) == 1:
            verse=chapter
            chapter=1
        # If the ref is in format: (Book, ?, None, None, #)
        # This normalizes references such as: Revelation 2-3
        elif end_verse:
            verse=1
            end_chapter=end_verse
            end_verse=None


    # Convert to integers or leave as None
    chapter = int(chapter) if chapter else None
    verse = int(verse) if verse else None
    end_chapter = int(end_chapter) if end_chapter else chapter
    end_verse = int(end_verse) if end_verse else None
    if not book \
    or (chapter is None or chapter < 1 or chapter > len(book[3])) \
    or (verse is not None and (verse < 1 or verse > book[3][chapter-1])) \
    or (end_chapter is not None and (
        end_chapter < 1
        or end_chapter < chapter
        or end_chapter > len(book[3]))) \
    or (end_verse is not None and(
        end_verse < 1
        or (end_chapter and end_verse > book[3][end_chapter-1])
        or (chapter == end_chapter and end_verse < verse))):
        raise InvalidReferenceException()
    
    if not verse:
        return (book[0], chapter, 1, chapter, book[3][chapter-1])
    if not end_verse: 
        if end_chapter and end_chapter != chapter:
            end_verse = book[3][end_chapter-1]
        else:
            end_verse = verse
    if not end_chapter:
        end_chapter = chapter
    return (book[0], chapter, verse, end_chapter, end_verse)

