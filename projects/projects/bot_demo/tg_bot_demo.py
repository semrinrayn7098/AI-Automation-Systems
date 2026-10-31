import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)

# ЗАГЛУШКА ТОКЕНА! Реальный токен вставлять нельзя в публичный репо.
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        "Я демонстрационный Python-бот.\n"
        "Пришли мне любое сообщение, и я отвечу тем же."
    )

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

async def main():
    if BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("⚠️ Warning: Set your real token in BOT_TOKEN variable!")
        return
    
    bot = Bot(token=BOT_TOKEN)
    print("🚀 Bot started.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped.")
