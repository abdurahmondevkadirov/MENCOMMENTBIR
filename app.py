from aiogram import executor
from time import sleep
from loader import dp, db,bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from data.config import ADMINS

async def on_startup(dispatcher):
    # Birlamchi komandalar (/start va /help)
    await set_default_commands(dispatcher)

    # Ma'lumotlar bazasini yaratamiz:
    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
async def on_shutdown(dispatcher):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text="❌Bot o'chdi")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,on_shutdown=on_shutdown)