import logging

from aiogram import Bot, Dispatcher, executor, types

from chatgpt import *

API_TOKEN = '6035234083:AAFg2O4tkqhpmtztfnm_3HQUxen_3Fcax1o'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    a = f'🤖 Привет, @{message.from_user.username}! Я бот ChatGPT!\n\n🔗 Вы можете задавать любые вопросы\n\nТакже бот иногда может грузить ответ в течении нескольких минут.\
 Все зависит от серверов на стороне OpenAI!\n\nСоветы к правильному использованию:\n– Задавайте осмысленные вопросы, расписывайте детальнее.\n– Не пишите ерунду иначе одержите её же в ответ.\n\n\
Примеры вопросов/запросов:\n~ Сколько будет 7 * 8?\n~ Когда началась Вторая Мировая?\n~ Напиши код калькулятора на Python\n~ Напиши сочинение как я провел лето\n\n\
🔥 Чтобы начать общение, напиши что-нибудь CHATGPT в строку ниже 👇🏻'
    await message.reply(a)


@dp.message_handler()
async def chat(message: types.Message):
    a = chat_ai(message.text)
    #print(message.text)
    #print(a)
    #print()
    await message.reply(a)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
