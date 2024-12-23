from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "8178893499:AAG4RSunJDSl1tggjIcpKVWyVQvawWLCKtE"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.row(button1, button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Начинаем', reply_markup=kb)

@dp.message_handler(text='Информация')
async def info_bot(message):
    await message.answer('Этот бот считает суточную норму калорий')

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer('Введите свой пол (М/Ж):')
    await UserState.gender.set()

@dp.message_handler(state=UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    if data['gender'] == "Ж":
        await message.answer(f'Ваша норма калорий: {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) - 161}')
    elif data['gender'] == "М":
        await message.answer(f'Ваша норма калорий: {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5}')
    else:
        await message.answer('Придется начать сначала, я еще не до конца разобралась')
    await state.finish()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Для того чтобы начать, введите /start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
