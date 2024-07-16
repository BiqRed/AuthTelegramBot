import hashlib
from typing import List

from config import TEXTS, DEFAULT_LANG


def create_hash(data: List[str]) -> str:
    """Create MD5 hash using secret key and data"""
    data = map(str, data)
    combined_string = '.'.join(data)
    md5 = hashlib.md5()
    md5.update(combined_string.encode())
    hash_hex = md5.hexdigest()

    return hash_hex


def check_hash(data: List[str], hash_: str) -> bool:
    """Check hash using secret key and data"""
    return create_hash(data) == hash_


def get_text(text: str, lang: str = None, user_lang: str = None) -> str:
    """Get text from TEXTS dictionary for specified language"""
    if lang and lang in TEXTS:
        return TEXTS[lang][text]
    if user_lang and user_lang in TEXTS:
        return TEXTS[user_lang][text]
    return TEXTS[DEFAULT_LANG][text]
