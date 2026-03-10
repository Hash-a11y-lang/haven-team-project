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
    await message.answer("Привет, я отсталый!")








































































async def main():
    print("Я запустился! Я отсталый!!!.") 
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("Пробую запустить бота...")
        asyncio.run(main())
    except Exception as e:
        print(f"ПРОИЗОШЛА ОШИБКА: {e}")
