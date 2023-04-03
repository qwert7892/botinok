from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ChatActions

import asyncio

import logging
from chatgpt import *

from settings import *

API_TOKEN = get_tgAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler()
async def echo(message: types.Message):
    #a = chat_ai(message.text)
    await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
    await asyncio.sleep(2)
    await bot.send_message(chat_id=message.chat.id, text='хуй')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)