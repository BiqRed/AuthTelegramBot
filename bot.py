import asyncio
from urllib.parse import urlencode, urljoin

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, CommandObject

from config import BOT_TOKEN, SECRET_KEY, REDIRECT_URL
from scripts import get_text, check_hash, create_hash

dp = Dispatcher()


@dp.message(CommandStart())
async def main_handler(message: types.Message, command: CommandObject) -> None:
    if not command.args:
        return
    data = command.args.split('-')
    if len(data) < 2:
        return

    hash_ = data[0]
    user_data = data[1]
    lang = data[2] if len(data) > 2 else None

    if not check_hash([SECRET_KEY, user_data], hash_):
        return

    params = {
        'data': user_data,
        'auth_at': int(message.date.timestamp()),
        'user_id': message.from_user.id,
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name
    }

    params['hash'] = create_hash([SECRET_KEY, *params.values()])

    await message.answer(
        get_text('message', lang, message.from_user.language_code),
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[[
                types.InlineKeyboardButton(text=get_text('button', lang, message.from_user.language_code),
                                           url=urljoin(REDIRECT_URL, '?' + urlencode(params)))
            ]]
        )
    )


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
