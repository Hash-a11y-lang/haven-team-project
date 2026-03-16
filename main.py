import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

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
            types.KeyboardButton(text="Звонки"),
            types.KeyboardButton(text="Уроки")
        ],
    ]    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите расписание"
    )
    await message.answer("Выберите тип расписания:", reply_markup=keyboard)





































































async def main():
    print("Я запустился! Я отсталый!!!.") 
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("Пробую запустить бота...")
        asyncio.run(main())
    except Exception as e:
        print(f"ПРОИЗОШЛА ОШИБКА: {e}")
