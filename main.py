import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state


from chatgpt import *

from db import *

API_TOKEN = '6035234083:AAFg2O4tkqhpmtztfnm_3HQUxen_3Fcax1o'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

file = open('db.txt', '+a')
file.close()


class Profile(StatesGroup):
    id = State()
    count = State()
    status = State()


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    a = f'🤖 Привет, @{message.from_user.username}! Я бот ChatGPT!\n\n🔗 Вы можете задавать любые вопросы\n\nТакже бот иногда может грузить ответ в течении нескольких минут.\
 Все зависит от серверов на стороне OpenAI!\n\nСоветы к правильному использованию:\n– Задавайте осмысленные вопросы, расписывайте детальнее.\n– Не пишите ерунду иначе одержите её же в ответ.\n\n\
Примеры вопросов/запросов:\n~ Сколько будет 7 * 8?\n~ Когда началась Вторая Мировая?\n~ Напиши код калькулятора на Python\n~ Напиши сочинение как я провел лето\n\n\
🔥 Чтобы начать общение, напиши что-нибудь CHATGPT в строку ниже 👇🏻'
    add_user(str(message.chat.id))
    await message.reply(a)


@dp.message_handler()
async def chat(message: types.Message):
    a = chat_ai(message.text)
    if add_user(str(message.chat.id)) is False:
        count_user(str(message.chat.id))
        if str(get_count(str(message.chat.id))) == '2':
            user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            print(user_status)
            #try:
                # Это для тех у кого есть фамилия
                # из-за этого элемент со статусом находится дальше
            #    if user_channel_status[70] != 'left':
            #        await bot.send_message(message.from_user.id, '')
                    # Пользователь уже подписан
            #    else:
            #        await bot.send_message(message.chat.id, '')
                    # Требуем подписки
            #except:
                # Для тех кто без фамилии
            #    if user_channel_status[60] != 'left':
            #        await bot.send_message(message.from_user.id, '')
                    # подписан
            #    else:
            #        await bot.send_message(message.from_user.id, '')
                    # Требуем подписки

        await message.reply(a)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
