import os

from aiogram import Bot, Dispatcher


from tg_bot.handlers.commands import router as commands_router


class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = Bot(Config.BOT_TOKEN)


dispatcher = Dispatcher()
dispatcher.include_router(commands_router)
