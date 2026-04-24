from aiogram import Bot, Dispatcher, types
import asyncio

BOT_TOKEN = "8235644002:AAGR6uaVjMVBuncwS_mqvSThLGjrp7MsobI"
CHANNEL_ID = "@shuraparfume"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

AUTO_TEXT = """

👤 Admin: @RF_shakhr
📞 Telefon: +998 91 778 26 81
📦 Hamma shaharga dastavka bor!📦
Buyurtma uchun admin bilan bog‘laning ✨
"""

@dp.message()
async def post_to_channel(message: types.Message):
    if message.photo:
        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=message.photo[-1].file_id,
            caption=(message.caption or "") + AUTO_TEXT
        )
    elif message.video:
        await bot.send_video(
            chat_id=CHANNEL_ID,
            video=message.video.file_id,
            caption=(message.caption or "") + AUTO_TEXT
        )
    else:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=(message.text or "") + AUTO_TEXT
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
