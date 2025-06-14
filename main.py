import aiogram
import asyncio

import aiogram.filters
import dotenv
import os

dotenv.load_dotenv()

bot = aiogram.Bot(os.getenv("BOT_TOKEN"))
dp = aiogram.Dispatcher()


@dp.message(aiogram.filters.Command("start"))
async def start_handler(message: aiogram.types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")


def on_start():
    print("Bot has been started...")


async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)


asyncio.run(main())
