import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import ChatNotFound
from utils.misc import subscription
from loader import bot
from data.config import ADMINS


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self,update:types.Update,data:dict):
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        with open("middlewares/banned_users.txt","r") as file:
            ids = file.read()
            ids = ids.split("/")
        logging.info(user)
        with open("middlewares\\bot_stop.txt","r") as file:
            active_nonActive=file.read()
        if int(active_nonActive)==0:
            
            if str(user) in ADMINS:
                pass
            else:
                await update.message.answer("⚙️Botda texnik ishlar olib borilyapti...")
                raise CancelHandler









        else:
            if str(user) in ids:
                await update.message.answer("<b>Siz botdan banlangansiz❌</b>\n\n\n<i>Agar bu shunmovchilik bo'lsa admin bilan bog'laning: @abdurahmondev</i>",disable_web_page_preview=True)
                # print(ids)
                raise CancelHandler()

            else:
                # print(ids)
                pass
                try:    
                    result = "Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling:\n"
                    final_status = True
                    CHANNELS = []
                    with open("data/channels.txt") as file:
                        channels=file.read()
                        list_channels = channels.split(",")
                        for channel in list_channels:
                            if channel!="":

                                CHANNELS.append(f"@{channel}")
                    for channel in CHANNELS:
                        status = await subscription.check(user_id=user,channel=channel)
                        final_status *= status
                        channel = await bot.get_chat(channel)
                        if not status:
                            invite_link = await channel.export_invite_link()
                            result += (f"👉 <a href = '{invite_link}'>{channel.title}</a>👈\n")
                    if not final_status:
                        await update.message.answer(result,disable_web_page_preview=True)
                        raise CancelHandler()
                except ChatNotFound:
                    pass
