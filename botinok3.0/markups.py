from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnSubed = KeyboardButton(text='ПОДПИСАЛСЯ ✅')
bot_sub_checker = ReplyKeyboardMarkup(resize_keyboard=True)
bot_sub_checker.add(btnSubed)