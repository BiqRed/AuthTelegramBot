# Telegram OAuth-like Authorization Bot
This bot serves as an authorization mechanism similar to Google OAuth but operates within Telegram. It authorizes users and redirects them to a specified URL with user information.

### How It Works:

1. Users are given a link to open the bot in Telegram: `https://t.me/<bot_nickname>?start=<params>`.
2. `params` is composed of `hash-data-lang`, where:
- hash is a MD5 hash generated from `secret_key.data`
- data is the information that will be returned in `redirect_url`. **Max length is 24 chars**.
- lang is a two-letter code determining the language to be used (all languages are specified in the TEXT variable in config.py).
3. After clicking a button in the bot, users are redirected to a configured URL with their details.
#### Example Bot Link:

> https://t.me/my_auth_bot?start=a1b2c3d4...e5f6-my_data-en

#### Redirect URL Example:

>https://your-redirect-url.com/callback?data=yoyr_data&username=johndoe&first_name=John&last_name=Doe&user_id=12345678&hash=a1b2c3d4e5f6...asda

### Configuration:

1. Set `REDIRECT_URL` (config.py) and `SECRET_KEY` in the bot's configuration file.
#### Env File `(.env)`:

```dotenv
BOT_TOKEN=xxxx:xxxxxxxxxx
SECRET_KEY=your_secret_key
```

# Running the Bot
#### pythonenv (python >3.8)
```bash
pip3 install -r requirements.txt
python3 bot.py
```

#### poetry (python 3.12)
```bash
poetry init
python3 bot.py
```

### Authorization Flow:

1. User clicks the bot link and opens the bot in Telegram.
2. The bot verifies the params using the `secret_key`.
3. If verification is successful, the bot provides a button for the user to click.
4. Upon clicking the button, the user is redirected to `redirect_url` with the following parameters:
- `data`: The information passed in the original `params`.
- `auth_at`: The time of authorization in UNIX format.
- `user_id`: The Telegram user ID.
- `username`: The Telegram username of the user.
- `first_name`: The first name of the user.
- `last_name`: The last name of the user.
- `hash`: A MD5 hash generated from `secret_key.data.auth_at.user_id.username.first_name.last_name`.
### Security:

The hash parameter ensures the integrity and authenticity of the user data being sent to the redirect URL:

> hash = md5(secret_key.data.auth_at.user_id.username.first_name.last_name)



## Example in Python
```python
import hashlib

SECRET_KEY = "your_secret_key"

def generate_link(bot_nickname: str, data: str, lang: str) -> str:
    if len(data) > 24:
        raise ValueError("Data length must be 24 characters or less.")
    hash_string = f"{SECRET_KEY}.{data}"
    hash_value = hashlib.md5(hash_string.encode()).hexdigest()
    params = f"{hash_value}-{data}-{lang}"
    return f"https://t.me/{bot_nickname}?start={params}"

def validate_response(
        data: str, auth_at: int, user_id: int, username: str, 
        first_name: str, last_name: str, received_hash: str
) -> bool:
    hash_string = f"{SECRET_KEY}.{data}.{auth_at}.{user_id}.{username}.{first_name}.{last_name}"
    expected_hash = hashlib.md5(hash_string.encode()).hexdigest()
    return expected_hash == received_hash
```


## Example in PHP
```php
<?php

define('SECRET_KEY', 'your_secret_key');

function generate_link($bot_nickname, $data, $lang) {
    if (strlen($data) > 24) {
        throw new Exception("Data length must be 24 characters or less.");
    }
    $hash_string = SECRET_KEY . '.' . $data;
    $hash_value = md5($hash_string);
    $params = $hash_value . '-' . $data . '-' . $lang;
    return "https://t.me/$bot_nickname?start=$params";
}

function validate_response($data, $auth_at, $user_id, $username, $first_name, $last_name, $received_hash) {
    $hash_string = SECRET_KEY . '.' . $data . '.' . $auth_at . '.' . $user_id . '.' . $username . '.' . $first_name . '.' . $last_name;
    $expected_hash = md5($hash_string);
    return $expected_hash === $received_hash;
}
?>
```
