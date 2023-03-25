from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnUrlChannel1 = InlineKeyboardButton(text="ПОДПИСАТЬСЯ", url="https://t.me/botinok_test")
btnDoneSub1 = InlineKeyboardButton(text="ПОДПИСАЛСЯ ✅", callback_data="subchanneldone1")

btnUrlChannel2 = InlineKeyboardButton(text="ПОДПИСАТЬСЯ", url="https://t.me/botinok_test3")
btnDoneSub2 = InlineKeyboardButton(text="ПОДПИСАЛСЯ ✅", callback_data="subchanneldone2")

checkSubMenu1 = InlineKeyboardMarkup(row_width=1)
checkSubMenu1.insert(btnUrlChannel1)
checkSubMenu1.insert(btnDoneSub1)

checkSubMenu2 = InlineKeyboardMarkup(row_width=1)
checkSubMenu2.insert(btnUrlChannel2)
checkSubMenu2.insert(btnDoneSub2)