import config
from aiogram.client.telegram import TelegramAPIServer
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot
from aiogram.enums import ParseMode
import openai_req


bot_token=config.TOKEN
admin_id = config.admin_id

if config.use_local_api:
    session = AiohttpSession(
            api=TelegramAPIServer.from_base(config.api_base_url)
    )
    bot = Bot(bot_token, session=session, parse_mode=ParseMode.HTML)
else:
    bot = Bot(bot_token, parse_mode=ParseMode.HTML)

is_running = True