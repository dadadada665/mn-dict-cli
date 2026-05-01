"""Cyrillic ↔ Latin transliteration helpers."""

CYRILLIC_TO_LATIN = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'ye', 'ё': 'yo', 'ж': 'j', 'з': 'z', 'и': 'i',
    'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'ө': 'ö', 'п': 'p', 'р': 'r', 'с': 's',
    'т': 't', 'у': 'u', 'ү': 'ü', 'ф': 'f', 'х': 'kh',
    'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
    'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
}


def to_latin(text: str) -> str:
    """Convert Mongolian Cyrillic to Latin transliteration."""
    if not text:
        return ''
    return ''.join(CYRILLIC_TO_LATIN.get(ch, ch) for ch in text.lower())


def is_cyrillic(text: str) -> bool:
    """Check if text contains Cyrillic characters."""
    return any('\u0400' <= ch <= '\u04ff' for ch in text)
