import logging
import markups as nav

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state

setts = open('settings.txt', encoding='utf-8').readlines()
key = setts[0].split()[1]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=key)
dp = Dispatcher(bot, storage=MemoryStorage())


class Profile(StatesGroup):
    answer = State()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('здарова заебал')
    await Profile.answer.set()


@dp.message_handler(state=Profile.answer)
async def echo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    await message.answer(message.text)
    await state.update_data(profile_answer=message.text)
    data = await state.get_data()
    print(data)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
