import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram import F

# Эта команда ищет файл .env и загружает данные из него
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
# ... далее код бота ...

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Понедельник"),
            types.KeyboardButton(text="Вторник"),
            types.KeyboardButton(text="Среда"),
            types.KeyboardButton(text="Четверг"),
            types.KeyboardButton(text="Пятница")
        ]
    ]    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите расписание"
    )


@dp.message(F.text == "Понедельник")
async def ring(message: types.Message):
    await message.answer("Тут будут звоночки")

@dp.message(F.text== "Вторник")
async def lession(message: types.Message):
    await message.answer("Вторник")

@dp.message(F.text== "Среда")
async def lession(message: types.Message):
    await message.answer("Среда")

@dp.message(F.text== "Четверг")
async def lession(message: types.Message):
    await message.answer("Четверг")

@dp.message(F.text== "Пятница")
async def lession(message: types.Message):
    await message.answer("Пятница")




























































async def main():
    print("Я запустился! Я отсталый!!!.") 
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("Пробую запустить бота...")
        asyncio.run(main())
    except Exception as e:
        print(f"ПРОИЗОШЛА ОШИБКА: {e}")
