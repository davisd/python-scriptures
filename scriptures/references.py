import re

from bible_re import testaments, book_re, scripture_re

class InvalidReferenceException(Exception):
    """
    Invalid Reference Exception
    """
    pass

def get_book(name):
    """
    Get a book from its name or None if not found
    """
    for books in testaments.itervalues():
        for book in books:
            if re.match(book[2], name, re.IGNORECASE):
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
    normalized = normalize_reference(bookname, chapter, verse,
                                              end_chapter, end_verse)
    if normalized[1]==normalized[3] and normalized[2]==1 and normalized[4] > 1:
        if get_book(normalized[0])[3][normalized[1]-1] == normalized[4]:
            return '{0} {1}'.format(normalized[0], normalized[1])
        
    tostring = '{0} {1}:{2}'.format(normalized[0], normalized[1], normalized[2])
    if not (normalized[1] == normalized[3] and normalized[2] == normalized[4]):
        if normalized[1] == normalized[3]:
            return tostring + '-{0}'.format(normalized[4])
        else:
            return tostring + '-{0}:{1}'.format(normalized[3], normalized[4])
    else:
        return tostring

def normalize_reference(bookname, chapter, verse=None,
                                  end_chapter=None, end_verse=None):
    """
    Get a complete five value tuple scripture reference with full book name
    from partial data
    """
    book = get_book(bookname)
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

