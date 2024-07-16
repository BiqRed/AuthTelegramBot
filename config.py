from os import getenv

# Load environment variables using python-dotenv
LOAD_DOTEND = True

if LOAD_DOTEND:
    from dotenv import load_dotenv
    load_dotenv()

# Telegram bot token from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN")
# Your secret key for checking hash signatures
SECRET_KEY = getenv("SECRET_KEY")

# Custom variable for TEXTS
SITE_URL = 'your-site-url.com'

# Bot texts for different languages
TEXTS = {
    'ru': {
        'message': f'''<b>Авторизация на сайте</b>
Нажмите на кнопку ниже, чтобы авторизоваться на сайте {SITE_URL}, используя Ваш аккаунт в Telegram. 
<i>{SITE_URL} получит доступ к Вашему никнейму, ID и полному имени.</i>

<u>Ссылка является одноразовой. Для повторной авторизации необходимо перейти по ссылке с сайте.</u>''',
        'button': 'Авторизоваться на сайте'
    },
    'en': {
        'message': f'''<b>Authorization on the Website</b>
Click the button below to log in to {SITE_URL} using your Telegram account.
<i>{SITE_URL} will gain access to your username, ID, and full name.</i>

<u>The link is one-time use only. To reauthorize, you will need to follow the link on the website again.</u>''',
        'button': 'Log in to the site'
    }
}

# Default language
DEFAULT_LANG = 'en'

# Redirect url to the site. Will contains data from the bot
REDIRECT_URL = 'https://my-cool-site.com/callback/telegram'
