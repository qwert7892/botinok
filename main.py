import logging
import markups as nav

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

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
    if password == '1':
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
        else:
            await bot.send_message(chat_id=message.chat.id, text='Несуществующая команда')
    else:
        await bot.send_message(chat_id=message.chat.id, text='Неверный пароль')


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    a = f'🤖 Привет, {message.from_user.first_name}! Я бот ChatGPT!\n\n🔗 Вы можете задавать любые вопросы\n\nТакже бот иногда может грузить ответ в течении нескольких минут.\
 Все зависит от серверов на стороне OpenAI!\n\nСоветы к правильному использованию:\n– Задавайте осмысленные вопросы, расписывайте детальнее.\n– Не пишите ерунду иначе одержите её же в ответ.\n\n\
Примеры вопросов/запросов:\n~ Сколько будет 7 * 8?\n~ Когда началась Вторая Мировая?\n~ Напиши код калькулятора на Python\n~ Напиши сочинение как я провел лето\n\n\
🔥 Чтобы начать общение, напиши что-нибудь CHATGPT в строку ниже 👇🏻'
    add_user(str(message.chat.id))
    await bot.send_message(chat_id=message.chat.id, text=a)


@dp.message_handler(lambda message: message.text == 'ПОДПИСАЛСЯ ✅')
async def got_sub(message: types.Message):
    status = False
    a = []
    for i in get_channels():
        if check_sub_channel(await bot.get_chat_member(chat_id=f'@{i}', user_id=message.from_user.id)):
            change_status(str(message.chat.id))
            a.append(True)
        else:
            a.append(False)
            await bot.send_message(chat_id=message.chat.id, text='Ты подписан не на все каналы')
            break
    status = True
    for i in a:
        if i is False:
            status = False
    if status is True:
        await bot.send_message(chat_id=message.chat.id,
                               text='Спасибо, теперь можете пользоваться ChatGPT неограниченно')


@dp.message_handler()
async def start_chat(message: types.Message):
    if add_user(str(message.chat.id)) is False and int(get_count(str(message.chat.id))) < 3:
        count_user(str(message.chat.id))

        if str(get_count(str(message.chat.id))) == '3':
            a = chat_ai(message.text)
            await bot.send_message(chat_id=message.chat.id, text=a)
            mes = ''
            channels = get_channels()
            for i in channels:
                mes += f'\n@{i}'
            MSG_NOT_FOLLOW = f'Чтобы продолжить использовать ChatGPT подпишись на эти каналы:' + mes
            await bot.send_message(chat_id=message.chat.id, text=MSG_NOT_FOLLOW, reply_markup=nav.bot_sub_checker)

        else:
            a = chat_ai(message.text)
            await bot.send_message(chat_id=message.chat.id, text=a)

    elif get_status(str(message.chat.id)) is True and int(get_count(str(message.chat.id))) >= 3:
        a = chat_ai(message.text)
        await bot.send_message(chat_id=message.chat.id, text=a, reply_markup=types.ReplyKeyboardRemove())


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
