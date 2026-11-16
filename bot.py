import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

# Loglarni yoqish
logging.basicConfig(level=logging.INFO)

# Sizning bot tokeningiz
TOKEN = "9144720823:AAGioU4PYfEwzSapQOojz1ioUCFpPSIsZIU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'iga javob
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu alaykum!")

# Boshqa matnlarga javob
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# Render uchun kichik veb-server
async def handle(request):
    return web.Response(text="Bot ishlayapti!")

app = web.Application()
app.router.add_get("/", handle)

async def web_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

# Bot va Veb-serverni birgalikda ishga tushirish
async def main():
    # Veb-serverni ishga tushiramiz
    await web_server()
    # Bot polling jarayonini boshlaymiz
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
