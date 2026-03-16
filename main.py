import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram import F

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

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
async def monday(message: types.Message):
    msg = (
        "📅 *Понедельник*\n\n"
        "```\n"
        "Предмет            | Время       | Каб.\n"
        "-------------------|-------------|-----\n"
        "Классный час       | 08:00-08:30 | 303\n"
        "Труд (технология)  | 08:35-09:10 | 108/104\n"
        "Физика             | 09:25-10:00 | 312\n"
        "Алгебра            | 10:20-10:55 | 303\n"
        "Биология           | 11:15-11:50 | 204\n"
        "История            | 12:00-12:35 | 139\n"
        "География          | 12:40-13:15 | 306\n"
        "```"
    )
    await message.answer(msg, parse_mode="MarkdownV2")

@dp.message(F.text== "Вторник")
async def tuesday(message: types.Message):
    msg = (
        "📅 *Вторник*\n\n"
        "```\n"
        "Предмет             | Время       | Каб.\n"
        "--------------------|-------------|-----\n"
        "Биология            | 08:00-08:40 | 214\n"
        "Геометрия           | 08:50-09:30 | 303\n"
        "Акт. вопр. матем.   | 09:45-10:25 | 303\n"
        "Физ. культура       | 10:45-11:25 | Зал\n"
        "Англ. язык          | 11:45-12:25 | 140/147\n"
        "Химия               | 12:35-13:15 | 212\n"
        "Русский язык        | 13:20-14:00 | 204\n"
        "```"
    )
    await message.answer(msg, parse_mode="MarkdownV2")

@dp.message(F.text == "Среда")
async def wednesday(message: types.Message):
    msg = (
        "📅 *Среда*\n\n"
        "```\n"
        "Предмет             | Время       | Каб.\n"
        "--------------------|-------------|-----\n"
        "География           | 08:00-08:40 | 306\n"
        "Информатика         | 08:50-09:30 | 310/317\n"
        "Физическая культура | 09:45-10:25 | Зал\n"
        "Алгебра             | 10:45-11:25 | 303\n"
        "Обществознание      | 11:45-12:25 | 207\n"
        "Русская словесность | 12:35-13:15 | 204\n"
        "Литература          | 13:20-14:00 | 204\n"
        "```"
    )
    await message.answer(msg, parse_mode="MarkdownV2")

@dp.message(F.text== "Четверг")
async def thursday(message: types.Message):
    msg = (
        "📅 *Четверг*\n\n"
        "```\n"
        "Предмет             | Время       | Каб.\n"
        "--------------------|-------------|-----\n"
        "Классный час        | 08:00-08:30 | 303\n"
        "Музыка              | 08:35-09:10 | 115\n"
        "Основы безопасн.    | 09:25-10:00 | 114\n"
        "Иностр. язык (англ) | 10:20-10:55 | 140/147\n"
        "Химия               | 11:15-11:50 | 212\n"
        "Алгебра             | 12:00-12:35 | 303\n"
        "Русский язык        | 12:45-13:20 | 204\n"
        "```"
    )
    await message.answer(msg, parse_mode="MarkdownV2")

@dp.message(F.text== "Пятница")
async def friday(message: types.Message):
    msg = (
        "📅 *Пятница*\n\n"
        "```\n"
        "Предмет             | Время       | Каб.\n"
        "--------------------|-------------|-----\n"
        "История             | 08:00-08:40 | 143\n"
        "Английский язык     | 08:50-09:30 | 140/147\n"
        "Физика              | 09:45-10:25 | 312\n"
        "Вероятн. и статист. | 10:45-11:25 | 303\n"
        "Геометрия           | 11:45-12:25 | 303\n"
        "Русский язык        | 12:35-13:15 | 204\n"
        "Литература          | 13:20-14:00 | 204\n"
        "```"
    )
    await message.answer(msg, parse_mode="MarkdownV2")





#Артемка, если ты смотришь этот код, привет тебе, ты лучший!!!






















































async def main():
    print("Я запустился! Я отсталый!!!.") 
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("Пробую запустить бота...")
        asyncio.run(main())
    except Exception as e:
        print(f"ПРОИЗОШЛА ОШИБКА: {e}")
