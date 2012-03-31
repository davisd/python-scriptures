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
    book=None

    normalized = normalize_reference(bookname, chapter, verse,
        end_chapter, end_verse)

    # if start and end chapters are the same
    if normalized[1] == normalized[3]:
        book = get_book(normalized[0])

        if len(book[3]) == 1: # single chapter book
            # If start and end verses are the same
            if normalized[2] == normalized[4]:
                return '{0} {1}'.format(*normalized[0::2])
            else:
                return '{0} {1}-{2}'.format(*normalized[0::2])
        else: # multichapter book
            # If the start verse is one and the end verse is the last verse in
            # the chapter
            if normalized[2] == 1 and normalized[4] == book[3][normalized[1]-1]:
                return '{0} {1}'.format(*normalized[:2])
            # If start and end verses are the same
            elif normalized[2] == normalized[4]:
                return '{0} {1}:{2}'.format(*normalized[:3])
            else:
                return '{0} {1}:{2}-{3}'.format(
                    *(normalized[:3] + normalized[-1:]))
    else: # start and end chapters are different
        return '{0} {1}:{2}-{3}:{4}'.format(*normalized)

def normalize_reference(bookname, chapter, verse=None,
                                  end_chapter=None, end_verse=None):
    """
    Get a complete five value tuple scripture reference with full book name
    from partial data
    """
    book = get_book(bookname)

    # SPECIAL CASE FOR BOOKS WITH ONE CHAPTER:
    # If there is only one chapter in this book, set the chapter to one and
    # treat the incoming chapter argument as though it were the verse.
    # This normalizes references such as:
    # Jude 2 and Jude 2-4
    if len(book[3]) == 1:
        if verse is None and end_chapter is None:
            verse=chapter
            chapter=1
    else:
        # This is not a single chapter book.
        # If a start verse was NOT provided, but an end_verse was- we have a
        # reference such as John 3-4 which is invalid.
        if verse is None and end_verse:
            raise InvalidReferenceException()

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

