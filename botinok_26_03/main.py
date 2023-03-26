import logging
import markups as nav

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state


from chatgpt import *

from db import *

def get_tgAPI():
    sf = open('settings.txt', 'r')
    setfile = sf.readlines()
    return setfile[0].split()[1]

def get_CH_ID1():
    sf = open('settings.txt', 'r')
    setfile = sf.readlines()
    return setfile[2].split()[1]

def get_CH_ID2():
    sf = open('settings.txt', 'r')
    setfile = sf.readlines()
    return setfile[3].split()[1]

API_TOKEN = get_tgAPI()
CH_ID1 = '@' + get_CH_ID1()
CH_ID2 = '@' + get_CH_ID2()
MSG_NOT_FOLLOW = 'Хорошо, сейчас я подумаю над твоим вопросом. А ты пока подпишись на канал:'

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
            if check_sub_channel(await bot.get_chat_member(chat_id=CH_ID1, user_id=message.from_user.id)):
                await bot.send_message(message.from_user.id, 'success!')
            else:
                await bot.send_message(message.from_user.id, MSG_NOT_FOLLOW, reply_markup=nav.checkSubMenu1)

        if str(get_count(str(message.chat.id))) == '4':
            if check_sub_channel(await bot.get_chat_member(chat_id=CH_ID2, user_id=message.from_user.id)):
                await bot.send_message(message.from_user.id, 'success!')
            else:
                await bot.send_message(message.from_user.id, MSG_NOT_FOLLOW, reply_markup=nav.checkSubMenu2)

        await message.reply(a)

def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False
    
@dp.callback_query_handler(text='subchanneldone1')
async def subchanneldone1(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CH_ID1, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'success!')
        change_status(str(message.from_user.id))
    else:
        await bot.send_message(message.from_user.id, MSG_NOT_FOLLOW, reply_markup=nav.checkSubMenu1)

@dp.callback_query_handler(text='subchanneldone2')
async def subchanneldone1(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CH_ID2, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'success!')
        change_status_2(str(message.from_user.id))
    else:
        await bot.send_message(message.from_user.id, MSG_NOT_FOLLOW, reply_markup=nav.checkSubMenu2)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
