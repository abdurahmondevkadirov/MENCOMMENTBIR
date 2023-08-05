# from typing import Text
# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandHelp
# import time as tm
# from loader import dp


# @dp.message_handler(commands=['send_db_to_abdurahmondev'])
# async def bot_help(message: types.Message):
#     nuqta = "..."
#     text = ("Admin assalomu alaykum tez orada bazadagi ma'lumotlar sizga taqdim etiladi"+nuqta)
    
#     message=await message.answer(text)
#     count=0
#     while count<10:
#         nuqta+="."
#         count+=1
#         print("Bitta")
#         tm.sleep(0.01)
#         await message.delete()
#         if len(nuqta)==4:
#             nuqta="."
#         text = ("Admin assalomu alaykum tez orada bazadagi ma'lumotlar sizga taqdim etiladi"+nuqta)
    
#         message=await message.answer(text)

#     await message.delete()
#     await message.answer('Tayyor!!!')
#     with open("data/main.db","rb") as file:

#         await message.answer_document(file)
        


