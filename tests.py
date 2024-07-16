from urllib.parse import urlparse, parse_qs

from scripts import create_hash, check_hash
from config import SECRET_KEY


BOT_URL = 'https://t.me/tgundrbot'


def create_link(data: str, lang: str) -> str:
    params = f'{create_hash([SECRET_KEY, data])}-{data}-{lang}'
    return f'{BOT_URL}?start={params}'


def check_redirect_link(link: str):
    data = parse_qs(urlparse(link).query)
    print(f'hash_correct={check_hash([SECRET_KEY, data["data"][0], data["auth_at"][0], data["user_id"][0], data["username"][0], data["first_name"][0], data["last_name"][0]], data["hash"][0])}')


if __name__ == '__main__':
    print(create_link(input('data: '), input('lang: ')))
    check_redirect_link(input('link: '))