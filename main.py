import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# Эта команда ищет файл .env и загружает данные из него
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
# ... далее код бота ...
async def main():
    print("Я запустился! Я отсталый!!!.") 
    await dp.start_polling(bot)
