import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.buttons import buttons as main_keyboards
from keyboards.inline.subscription import check_button
from loader import dp, db, bot
from utils.misc import subscription
@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz


    # await message.answer(f"Xush kelibsiz {message.from_user.full_name}!")
    # Adminga xabar beramiz
    channels_format = str()
    CHANNELS = []
    with open("data/channels.txt") as file:
        channels=file.read()
        list_channels = channels.split(",")
        for channel in list_channels:
            if channel!="":
                CHANNELS.append(f"@{channel}")
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()

        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        all_users=db.select_all_users()[0]
        users_count = len(all_users)
        user_data = await bot.get_chat(message.from_user.id)
        text = f"➕Yangi user!Botda {users_count}ta bo'ldik\n"
        full_name = user_data.first_name
        bio = user_data.bio
        username = user_data.username
        full_name = user_data.full_name
        text+=f"""
    🆔Foydalanuvchi idsi: <code>{message.from_user.id}</code>
    📛Foydalanuvchi nomi: <code>{full_name}</code>
    🌐Foydalanuvchi useri: @{username}
    📍Foydalanuvchi biosi: <code>{bio}</code>"""
        await bot.send_message(chat_id=ADMINS[0], text=text)
    except sqlite3.IntegrityError as err:
        # await bot.send_message(chat_id=ADMINS[0], text=err)
        pass

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    a = True
    CHANNELS = []
    with open("data/channels.txt") as file:
        channels=file.read()
        list_channels = channels.split(",")
        for channel in list_channels:
            if channel!="":
                CHANNELS.append(f"@{channel}")
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"

        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
            a = False
            
    await call.message.answer(result, reply_markup=check_button, disable_web_page_preview=True)

    await call.message.answer("Harakatlardan birni tanlang!",reply_markup=main_keyboards)



