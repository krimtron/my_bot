import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import time 

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6977539871:AAHzRM2c3_td94pVwLfY0ZIVpC1XfcsW17Q")
# Диспетчер
dp = Dispatcher()


from datetime import datetime


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! Я перший бот на Python! Більше інформації про мене тут /help")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Стартовые команды: /hello, /time")
    
@dp.message(Command("hello"))
async def cmd_hello(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"Привет: {user_name}!")
    
@dp.message(Command("time"))
async def cmd_time(message: types.Message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await message.answer(f"Поточний час: {current_time}")

# @dp.message(Command("rep"))
# async def cmd_time(message: types.Message):
#     markup = types.ReplyKeyboardMarkup()
#     button = types.KeyboardButton("Yes")
#     button1 = types.KeyboardButton("No")
#     await message.answer("frds",reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())