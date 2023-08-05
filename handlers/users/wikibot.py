import logging
from aiogram.types import CallbackQuery,Message,ParseMode
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from test_data import PlayerFinderWithName,PlayerFinderWithStats
from keyboards.default.buttons import buttons,button_back,inline_adminrply,inline_userrply,admin_tugma,panel_tugma,tugmasi,tugmasi_rek,tugmasi_user,channel_tools
from keyboards.default.buttons import ban_tools,data_dls_bot_unmute,ortga_to_panel
from datetime import datetime
from loader import dp,db,bot
from data.config import ADMINS,BOT_START_DAY,BOT_NAME
from time import sleep
def number_to_stick(number):
    number = str(number)
    if "1" in number:
        number = number.replace("1","1️⃣")
    if "2" in number:
        number = number.replace("2","2️⃣")
    if "3" in number:
        number = number.replace("3","3️⃣")
    if "4" in number:
        number = number.replace("4","4️⃣")
    if "5" in number:
        number = number.replace("5","5️⃣")
    if "6" in number:
        number = number.replace("6","6️⃣")
    if "7" in number: 
        number = number.replace("7","7️⃣")
    if "8" in number:
        number = number.replace("8","8️⃣")
    if "9" in number:
        number = number.replace("9","9️⃣")
    if "0" in number:
        number = number.replace("0","0️⃣")
    return number
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
                            
    await message.answer("DLS futbolchi topuvchi botga xush kelibsiz!Futbolchi haqida ma'lumot kiritsangiz men u futbolchi(lar)ni topib beraman!",reply_markup=buttons)

@dp.message_handler(text_contains = "🔍Futbolchi ismi yoki familiyasiga ko'ra topish")
async def find_player_with_name(message: types.Message,state:FSMContext):
    
                            
    await message.answer("""Yaxshi futbolchi ismi yoki familiyasi aniq futbolchini topmoqchi bo'lsangiz ism+familiya shaklida yozing!\n\n🏴󠁧󠁢󠁥󠁮󠁧󠁿 Unutmang ism yoki familiya Inglizchada bolishi kerak masalan:

❌Holand  — ✅Haaland
❌Kilian  — ✅Kylian
❌Vinisius  — ✅Vinicius
❌Saloh  — ✅Salah
❌Muhammad  — ✅Mohamed
❌Rays  — ✅Rice
❌Tripper — ✅Trippier



❌E'tibor bering agar xato yozgan bolsangiz bot topib bermaydi!""",reply_markup=button_back)
    await state.set_state("player_name_surname")
@dp.message_handler(state="player_name_surname")
async def player_surname_name(message:types.Message,state:FSMContext):
    if message.text!="🔙 Ortga":
        await message.answer("Yaxshi.Hozir men sizga bu futbolchi haqida ma'lumot topib beraman!")
        data_players = PlayerFinderWithName(message.text)
        rezultatlar = len(data_players)
        print(data_players)
        matn = f"Qidirgan futbolchingizga ko'ra {rezultatlar}ta ma'lumot topildi👆!"
        count = 0
        for data_player in data_players:
            count+=1
            ism = data_player[0]
            familiya =data_player[1]
            narx =data_player[2]
            millat =data_player[3]
            klub =data_player[4]
            pozitsiya =data_player[5]
            oyoq = data_player[6]
            baholanish = data_player[7]
            boyi = data_player[8]
            tezlik = data_player[9]
            tezlanish = data_player[10]
            bardoshlilik = data_player[11]
            boshqaruv = data_player[12]
            kuch = data_player[13]
            hal_qilish =data_player[14]
            pass_berish = data_player[15]
            udar = data_player[16]
            rasm_id = data_player[17]
            matn_futbolchi = f"{count}.{ism} {familiya}:\n        💰Narxi: {narx}\n        🏞Millat: {millat}\n        ⛳️Klub: {klub}\n        ⚽️Pozitsiya: {pozitsiya}\n        🦵Oyoq: {oyoq}\n        🎖Baholanish: {baholanish}\n        🖊Bo'y :{boyi}\n        ⚡️Tezlik: {tezlik}\n        🔋Tezlanish: {tezlanish}\n         🧗‍♂️Bardoshlilik: {bardoshlilik}\n         🎛Boshqaruv: {boshqaruv}\n         💪Kuch: {kuch}\n         🫵Qaror qabul qilish: {hal_qilish}\n         🅰️Pass berish: {pass_berish}\n         🌠Udar: {udar}\n"
            
            if rasm_id:


                await bot.send_photo(chat_id=message.from_user.id,photo=open(f"photos/{rasm_id}.png","rb"),caption=f"{matn_futbolchi}",reply_markup=button_back)
            else:
                await bot.send_message(chat_id=message.from_user.id,text=matn_futbolchi,reply_markup=button_back)
        await message.answer(matn)
        try:
            await bot.send_message(chat_id=ADMINS[0],text=f"🙍‍♂️Foydalanuvchi : <a href='https://t.me/{message.from_user.username}'>{message.from_user.full_name}</a>\n🔍Qidirgan futbolchi(lar)i haqida statistika:\n{matn_futbolchi}🔎Qidirirgan uslubi:  ismga ko'ra qidirish")
        except:
            pass 
    else:
        await message.answer("Yaxshi menyulardan birini tanlang!",reply_markup=buttons)
        await state.finish()


@dp.message_handler(text="🔎Uning statistikasi bo'yicha topish!")
async def player_stats(message:types.Message,state:FSMContext):
    await message.answer("⚡️Tezlik(SPEed)ni yuboring(raqamda):",reply_markup=button_back)
    await state.set_state("speed")
@dp.message_handler(state="speed")
async def player_speed(message:types.Message,state:FSMContext):
    if message.text=="🔙 Ortga":
        await message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=buttons)
        await state.finish()
    else:
        await state.update_data({f"{message.from_user.id}_speed":{"speed":message.text}})
        await message.answer("🔋Tezlanish(ACCeleration)ini yuboring(raqamda):",reply_markup=button_back)
        await state.set_state("acceleration")
@dp.message_handler(state="acceleration")
async def player_acceleration(message:types.Message,state:FSMContext):
    if message.text=="🔙 Ortga":
        await message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=buttons)
        await state.finish()
    else:
        await state.update_data({f"{message.from_user.id}_acceleration":{"acceleration":message.text}})
        await message.answer("🧗‍♂️Bardoshlilik(STAmina)ini yuboring(raqamda):",reply_markup=button_back)
        await state.set_state("stamina")
@dp.message_handler(state="stamina")
async def player_acceleration(message:types.Message,state:FSMContext):
    if message.text=="🔙 Ortga":
        await message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=buttons)
        await state.finish()
    else:
        await state.update_data({f"{message.from_user.id}_stamina":{"stamina":message.text}})
        await message.answer("🎛Boshqaruv(CONtrol)ini yuboring(raqamda):",reply_markup=button_back)
        await state.set_state("control")
   

@dp.message_handler(state="control")
async def player_acceleration(message:types.Message,state:FSMContext):
    if message.text=="🔙 Ortga":
        await message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=buttons)
        await state.finish()
    else:
        await state.update_data({f"{message.from_user.id}_control":{"control":message.text}})
        await message.answer("💪Kuch(STRength)ini yuboring(raqamda):",reply_markup=button_back)
        await state.set_state("strength")
@dp.message_handler(state="strength")
async def player_acceleration(message:types.Message,state:FSMContext):
    if message.text=="🔙 Ortga":
        await message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=buttons)
        await state.finish()
    else:
        await state.update_data({f"{message.from_user.id}_strength":{"strength":message.text}})
        await message.answer("🫵Qaror qabul qilishini(TACkling)ini yuboring(raqamda):",reply_markup=button_back)
        await state.set_state("tackling")
@dp.message_handler(state="tackling")
async def player_acceleration(message:types.Message,state:FSMContext):
    if message.text=="🔙 Ortga":
        await message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=buttons)
        await state.finish()
    else:
        await state.update_data({f"{message.from_user.id}_tack":{"tackling":message.text}})
        await message.answer("🅰️Pass berish(PASsing)ini yuboring(raqamda):",reply_markup=button_back)
        await state.set_state("passing")
@dp.message_handler(state="passing")
async def player_acceleration(message:types.Message,state:FSMContext):
    if message.text=="🔙 Ortga":
        await message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=buttons)
        await state.finish()
    else:
        await state.update_data({f"{message.from_user.id}_pass":{"passing":message.text}})
        await message.answer("🌠Udar(SHOoting)ini yuboring(raqamda):",reply_markup=button_back)
        await state.set_state("shooting")
@dp.message_handler(state="shooting")
async def player_acceleration(message:types.Message,state:FSMContext):
    await state.update_data({f"{message.from_user.id}_shoot":{"shooting":message.text}})  
    data = await state.get_data()
    speed_data = data.get(f"{message.from_user.id}_speed")
    speed = speed_data.get("speed")
    acceleration_data = data.get(f"{message.from_user.id}_acceleration")
    acceleration = acceleration_data.get("acceleration")
    stamina_data = data.get(f"{message.from_user.id}_stamina")
    stamina = stamina_data.get("stamina")
    control_data = data.get(f"{message.from_user.id}_control")
    control = control_data.get("control")
    strength_data = data.get(f"{message.from_user.id}_strength")
    strength = strength_data.get("strength")
    tackling_data = data.get(f"{message.from_user.id}_tack")
    tackling = tackling_data.get("tackling")
    passing_data = data.get(f"{message.from_user.id}_pass")
    passing = passing_data.get("passing")
    shooting_data = data.get(f"{message.from_user.id}_shoot")
    shooting =shooting_data.get("shooting")
    
    player_names,updated_player_names = PlayerFinderWithStats(speed,acceleration,stamina,control,strength,tackling,passing,shooting)
    count = 0
    count_2 = 0
    royhat = ""
    royhat_2 = ""
    for player_name in player_names:
        count+=1
        ism = player_name[0]
        familiya = player_name[1]
        royhat+=f"\n{count}.{ism} {familiya}"
    for updated_player_name in updated_player_names:
        count+=1
        ism = updated_player_name[0]
        familiya = updated_player_name[1]
        royhat+=f"\n{count}.{ism} {familiya}"


    await message.answer(f"⚽️Futbolchi haqida ma'lumotlar:\n       ⚡️Tezlik: {speed}\n        🔋Tezlanish: {acceleration}\n        🧗‍♂️Bardoshlilik: {stamina}\n       🎛Boshqaruv: {control}\n       💪Kuch: {strength}\n       🫵Qaror qabul qilish: {tackling}\n       🅰️Pass berish: {passing}\n       🌠Udar: {shooting}\n\n\n⚔️Ushbu ma'lumotlarga mos keluvchi yoki yaqin keluvchi {count}ta futbolchi topildi:{royhat}")
    await bot.send_message(chat_id=ADMINS[0],text=f"🙍‍♂️Foydalanuvchi : <a href='https://t.me/{message.from_user.username}'>{message.from_user.full_name}</a>\n🔍Qidirgan futbolchi(lar)i haqida statistika:\n📊Statistika boyicha qidirildi:\n       Mos kelgan: {royhat}\n       Yaqin Kelgan: {royhat_2}")
    await state.finish()
@dp.message_handler(text_contains = "📞 Admin bilan muloqot")
async def consider_withadmin(msg:types.Message,state:FSMContext):
    await msg.answer("✍️Adminga xabaringizni yozib qoldiring!\n\n\nMisol:<code>Salom ...</code>")
    await state.set_state("adminmsg")
@dp.message_handler(state="adminmsg")
async def send_amdinmsg(message:types.Message,state:FSMContext):
    global user_id
    hozir = datetime.now()
    await message.answer("❓Savolingizga tez orada javob keladi!")
    user_id = message.from_user.id
    for admin in ADMINS:

         await bot.send_message(chat_id=admin,text=f"📅Xabar sanasi: {hozir.date()}\n⏱Xabar vaqti: {hozir.hour}:{hozir.minute}:{hozir.second}\n✍️Xabar matni: {message.text}\n🙍‍♂️Xabar muallifi: <a href='https://t.me/{message.from_user.username}'>{message.from_user.full_name}</a>\n🆔Xabar muallifi idsi:{message.from_user.id}\n💬Turi: Savol\n🟢Holati: Adminga savol jo'natildi✅",reply_markup=inline_adminrply)
         
    

    await state.finish()    
@dp.callback_query_handler(text="adminusermsg")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✍️Foydalanuvchiga xabaringizni yozib qoldiring!\n\n\nMisol:<code>Salom ...</code>")
    await state.set_state("usermsg")
@dp.message_handler(state="usermsg")
async def adminusermsg2(msg:types.Message,state:FSMContext):
    hozir = datetime.now()
    await msg.answer(f"📅Xabar sanasi: {hozir.date()}\n⏱Xabar vaqti: {hozir.hour}:{hozir.minute}:{hozir.second}\n✍️Xabar matni: {msg.text}\n🙍‍♂️Xabar muallifi: <a href='https://t.me/{msg.from_user.username}'>👨‍💻 Bot admini</a>\n💬Turi: Javob\n🟢Holati: Foydalanuvchi javob jo'natildi✅")
    await bot.send_message(chat_id=user_id,text=f"Admindan savolingizga javob✅\n\n\n<code>{msg.text}</code>",reply_markup=inline_userrply)
    await state.finish()
@dp.callback_query_handler(text = "useradminmsg")
async def consider_withadmin(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✍️Adminning xabariga javobingizni yozing!")
    await state.set_state("usermsg2")
@dp.message_handler(state="usermsg2")
async def useradmin(msg:types.Message,state:FSMContext):
    
    await msg.answer("Adminga javobiga yozilgan javob qabul qilindi va adminga jo'natildi✅")
    hozir = datetime.now()
    for admin in ADMINS:
        await bot.send_message(chat_id=admin,text=f"<a href='https://t.me/{msg.from_user.username}'>{msg.from_user.full_name}</a>ga yozgan xabaringizga javob keldi✅\n\n\n📅Xabar sanasi: {hozir.date()}\n⏱Xabar vaqti: {hozir.hour}:{hozir.minute}:{hozir.second}\n✍️Xabar matni: {msg.text}\n🙍‍♂️Xabar muallifi: <a href='https://t.me/{msg.from_user.username}'>{msg.from_user.full_name}</a>\n🆔Xabar muallifi idsi:{msg.from_user.id}\n💬Turi: Savol\n🟢Holati: Adminga savol jo'natildi✅",reply_markup=inline_adminrply)
    await state.finish()
@dp.callback_query_handler(text = "cancelled")
async def consider_withadmin(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("Uzr admin nojuaya xabar yuborgan foydalanuvchini nega xabarini o'chirayotganingizni yozib qoldiring!")
    await state.set_state("cancelled_sabab")
@dp.message_handler(state="cancelled_sabab")
async def useradmin(msg:types.Message,state:FSMContext):
    sabab_message = msg.text
    await bot.send_message(chat_id=user_id,text=f"❌ Xabaringiz rad etildi!Sabab:\n\n\n<code>{sabab_message}</code>")
    await msg.answer("🔕Yaxshi foydalanuvchini ogohlatirdim!")
    await state.finish()
@dp.callback_query_handler(text="ban")
async def ban(call:CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    if str(user_id) in ADMINS:
        await call.message.answer("❌Adminga ban bera olmaysiz(ADMINS royhatidan idni o'chiring va keyin ban bering!)")
    else:
        await call.message.answer("❌Yaxshi foydalanuvchi banlandi!")

        with open("middlewares/banned_users.txt","a+") as file:
            
            file.write(f"{user_id}/")

        await bot.send_message(chat_id=user_id,text="❌Siz botda banlandingiz")

@dp.message_handler(text="📊 Statistika")
async def stats_users(msg:types.Message):

    hozir = datetime.now()
    hour = str(hozir.hour)
    minute =str(hozir.minute)
    second = str(hozir.second)
    if len(hour) == 1:hourhoz="0"+hour
    else:hourhoz = hour
    if len(minute) == 1:minutehoz="0"+minute
    else:minutehoz = minute
    if len(second) == 1:secondhoz="0"+second
    else:secondhoz = second

    await msg.answer(f"📊Botimiz statistikasi:\n\n        👥A'zolar soni:{db.count_users()[0]}\n        ⏰Bot ishga tushgan sana: {BOT_START_DAY}\n        📅Hozirgi vaqt: {hozir.date()}\n        🤖Bot useri: {BOT_NAME}\n        ⏰Hozirgi vaqt: {hourhoz}:{minutehoz}:{secondhoz}\n\n👨‍💻Bot adminlari: \n        🙍‍♂️@Leo_Messi_ParisSaintGerman - 💻Sun'iy intellekt\n        🙍‍♂️@abdurahmondev - 🤖Bot dasturchi ")
@dp.message_handler(text_contains = "🔙 Ortga")
async def find_player_with_name(message: types.Message,state:FSMContext):
    await message.answer("Tanlang!",reply_markup=buttons)

@dp.message_handler(text_contains = "/admin")
async def find_player_with_name(message: types.Message,state:FSMContext):
    await message.answer("Bosing!",reply_markup=admin_tugma)



@dp.callback_query_handler(text="admin_panel")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    
    await call.message.answer("Assalomu alaykum sizni admin panelga kirishga ruxsatingiz bormi yo'qmi tekshirilyapti kuting...")
    sleep(2)
    user_id = call.from_user.id
    if int(ADMINS[0]) == int(user_id):
        await call.message.answer("✅Admin ekanligingiz tasdiqlandi!",reply_markup=panel_tugma)
    else:
        await call.message.answer("❌Afsus siz admin panelga kira olmaysiz")



@dp.callback_query_handler(text="rek_user_message")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("📩Reklama & 👤Userga xabar",reply_markup=tugmasi)
@dp.callback_query_handler(text="rek_xb")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("📩Reklama",reply_markup=tugmasi_rek)

@dp.callback_query_handler(text="user_xb")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("👤Userga xabar",reply_markup=tugmasi_user)









@dp.callback_query_handler(text="oddiy_xb_rek")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✍️Yaxshi xabarni menga jo'nating!")

    await state.set_state("xabar")
@dp.message_handler(state="xabar",content_types=["any"])
async def xb_func(message:types.Message,state:FSMContext):
    await state.finish()
    users = db.select_all_users()

    message_text = message.text
    count = 0 
    for user in users:
        user_id = user[0]
        try: 
            await bot.send_message(chat_id=user_id, text=message_text)
            sleep(0.05)
        except:
            count+=1
    await message.answer(f"🤖Botda {len(users)}ta obunachi bor:\n        ◾️{count} ta foydalanuvchi botni bloklagani sabali xabar jonatilmadi!\n        ◽️{int(len(users))-int(count)}ta foydalanuvchiga xabar jo'natildi",reply_markup=ortga_to_panel)


@dp.callback_query_handler(text="forward_xb_rek")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()

    await call.message.answer("💬Yaxshi forward xabarni menga jo'nating!")

    await state.set_state("frward_xb")
@dp.message_handler(state="frward_xb",content_types=["any"])
async def send_to_me(message:types.Message,state:FSMContext):
    await state.finish()

    users = db.select_all_users()
    message_text = message.text
    count = 0
    for user in users:
        user_id = user[0]
        try: 

            await bot.forward_message(chat_id=user_id, from_chat_id=ADMINS[0], message_id=message.message_id)
            sleep(0.005)
        except Exception as e:
            count+=1
            print(e)
    await message.answer(f"🤖Botda {len(users)}ta obunachi bor:\n        ◾️{count} ta foydalanuvchi botni bloklagani sabali xabar jonatilmadi!\n        ◽️{int(len(users))-int(count)}ta foydalanuvchiga xabar jo'natildi",reply_markup=ortga_to_panel)
    await state.finish()




@dp.callback_query_handler(text="oddiy_xb_user")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()

    await call.message.answer("🆔Foydalanuvchi idsini kiriting!")

    await state.set_state("xabar_user_id")

@dp.message_handler(state="xabar_user_id")
async def xb_user_id(message:types.Message,state:FSMContext):
    await state.update_data({f"{message.from_user.id}":message.text})

    await message.answer("✍️Yaxshi endi xabar matnini menga jo'nating!")

    await state.set_state("xabar_007")
@dp.message_handler(state="xabar_007")
async def xb_hammaga(message:types.Message,state:FSMContext):
    await state.finish()
    state_data = await state.get_data(f"{message.from_user.id}")
    users = db.select_all_users()
    message_text = message.text
    user_id = state_data.get(f"{message.from_user.id}")
    try:
        await bot.send_message(chat_id=user_id, text=message_text)
        await message.answer(f"🤖Botda {user_id} id egasiga xabar yubordingiz:\n        ◽️{user_id} id egasiga xabar yuborildi.U botni bloklamagan",reply_markup=ortga_to_panel)

    except:
        await message.answer(f"🤖Botda {user_id} id egasiga xabar yubordingiz:\n        ◾️{user_id} id egasi ta foydalanuvchi botni bloklagani sabali xabar jonatilmadi!",reply_markup=ortga_to_panel)



@dp.callback_query_handler(text="forward_xb_user")
async def send_ad_to_all__(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()

    await call.message.answer("🆔Foydalanuvchi idsini kiriting!")

    await state.set_state("xb_frwrd_user_id")

@dp.message_handler(state="xb_frwrd_user_id")
async def player_speed(message:types.Message,state:FSMContext):
    await state.update_data({f"{message.from_user.id}":message.text})

    await message.answer("✍️Yaxshi endi xabar matnini menga jo'nating!")

    await state.set_state("xabar_007_user")
@dp.message_handler(state="xabar_007_user")
async def send_to_all_(message:types.Message,state:FSMContext):
    state_data = await state.get_data(f"{message.from_user.id}")
    users = db.select_all_users()
    message_text = message.text
    await state.finish() 

    user_id = state_data.get(f"{message.from_user.id}")
    try:
        await bot.forward_message(chat_id=user_id, from_chat_id=ADMINS[0], message_id=message.message_id)
        await message.answer(f"🤖Botda {user_id} id egasiga xabar yubordingiz:\n        ◽️{user_id} id egasiga xabar yuborildi.U botni bloklamagan",reply_markup=ortga_to_panel)

    except:
        await message.answer(f"🤖Botda {user_id} id egasiga xabar yubordingiz:\n        ◾️{user_id} foydalanuvchi botni bloklagani sabali xabar jonatilmadi!",reply_markup=ortga_to_panel)


              
@dp.callback_query_handler(text="new_channel")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("<b>✍️Yaxshi kanal userini menga jo'nating</b>!\n\n<i>*Unutmang kanal userida @ bu belgi qatnashmasligi shart!</i>")

    await state.set_state("channels")
@dp.message_handler(state="channels")
async def deleteAllChannels(message:types.Message,state:FSMContext):
    with open("data/channels.txt","a+") as file:
        channels = file.read()
        channels+=f",{message.text}"
        file.write(channels)
    await message.answer("✅Kanalingiz muvaffaqiyatli qo'shildi!",reply_markup=ortga_to_panel)
    
    await state.finish()



@dp.callback_query_handler(text="del_all_channels")
async def player_speed(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    with open("data/channels.txt","w+") as file:
        file.write("")
    await call.message.answer("✅Barcha kanallar royhatdan o'chirildi",reply_markup=ortga_to_panel)
    
@dp.callback_query_handler(text="channels_list")
async def list_channels(call:CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    with open("data/channels.txt","r") as file:
        read_file = file.read()
        read_file_list = read_file.split(",")
        matn = ""
        count = 0
        for channel in read_file_list:

            if channel!="":
                count+=1
                matn+=f"\n      {count}.👉@{channel}👈"

        await call.message.answer(f"📡Kanallar royhati:{matn}",reply_markup=ortga_to_panel)







@dp.callback_query_handler(text="bot_off")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.answer(cache_time=30)
    await call.message.answer("❌Yaxshi admin bot o'chirildi.",reply_markup=ortga_to_panel)
    with open("middlewares/bot_stop.txt","w") as file:
        file.write("0")
@dp.callback_query_handler(text="bot_on")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✅Yaxshi admin bot yoqildi.",reply_markup=ortga_to_panel)
    with open("middlewares/bot_stop.txt","w") as file:
        file.write("1")
@dp.callback_query_handler(text="ban_man")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🆔Foydalanuvchi id raqamini  kiriting:")
    await state.set_state("to_ban_user_id")
@dp.message_handler(state="to_ban_user_id")
async def banMAN(message:types.Message,state:FSMContext):
    user_id = message.text
    with open("middlewares/banned_users.txt","r+") as file:
        idlar = file.read()
        idlar = idlar.split("/")
        if str(user_id) in idlar:
            await message.answer("🚷Foydalanuvchi allaqachon banlangan!",reply_markup=ortga_to_panel)
        else:
            file.write(f"{user_id}/")
            await message.answer("🚷Foydalanuvchi banlandi",reply_markup=ortga_to_panel)
            await bot.send_message(chat_id=user_id,text="❌Siz botda banlandingiz")


    
    await state.finish()
@dp.callback_query_handler(text="unban_man")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🆔Foydalanuvchi id raqamini  kiriting:")
    await state.set_state("to_unban_user_id")

@dp.message_handler(state="to_unban_user_id")
async def banMAN(message:types.Message,state:FSMContext):
    user_id = message.text
    with open("middlewares/banned_users.txt","r") as file:
        file_data = file.read()
        user_ids = file_data.split("/")
        for user_id1 in user_ids:
            if str(user_id1) == str(user_id):
                a = True
                break
            else:
                a = False

        if a:

            user_ids.remove(user_id)
            await bot.send_message(chat_id=user_id,text=f"Siz botdan bandan olindizgiz.")
            await message.answer("Yaxshi foydalanuvchi bandan olindi!",reply_markup=ortga_to_panel)
        else:
            await message.answer("Foydalanuvchi avval ham banda emasdi!",reply_markup=ortga_to_panel)     
        matn = ""
        for user_id_new in user_ids:
            matn+=f"{user_id_new}/"
        print(matn)
    with open("middlewares/banned_users.txt","w") as file:

        file.write(matn)
    await state.finish()



@dp.callback_query_handler(text="download_db")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("Yaxshi admin bazani sizga yuboraman")
    count = db.count_users()[0]
    await call.message.answer_document(open("data/main.db","rb"),caption=f"Bot bazasi:\n       🙍‍♂️🙍‍♂️Azolar soni: {count}",reply_markup=ortga_to_panel)


@dp.callback_query_handler(text="unban_men")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✅Barcha foydalanuvchilar bandan olindi",reply_markup=ortga_to_panel)
    with open("middlewares/banned_users.txt","w") as file:
        pass 
@dp.callback_query_handler(text="del_channel")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("📛Kanal userini kiriting(@ qatnashmagan holda):")
    await state.set_state("channel_username")
@dp.message_handler(state="channel_username")
async def DelChannel(message:types.Message,state:FSMContext):
    with open("data/channels.txt","r") as file:
        file_data = file.read()
        channel_users = file_data.split(",")

        for channel_user in channel_users:
            if str(channel_user) == str(message.text):
                a = True

                channel_users.remove(channel_user)
                break
            else:
                a = False
                print(channel_user,message.text)

        if a:
            await message.answer("➖Yaxshi kanal ro'yhatdan chiqarib tashlandi",reply_markup=ortga_to_panel)
            matn = ""
            with open("data/channels.txt","w") as file:
                for channel_user in channel_users:
                    matn+=f",{channel_user}"


        else:
            await message.answer("❌Bunday kanal ro'yhatda mavjud emas",reply_markup=ortga_to_panel)
        await state.finish()
@dp.callback_query_handler(text="change_data_dls")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("Menga data dls faylini yuboring unutmang fayl python yordamida yaratilgan va futbolchilar ushbu shaklda saqlangan bolishi kerak:\n\n<code>data = [{"":""},...]</code>",reply_markup=button_back)
    await state.set_state("recieve_file")


@dp.message_handler(state="recieve_file",content_types=['any'])
async def DelChannel(message:types.Message,state:FSMContext):
    if message.content_type == 'document':
        await message.answer("✅Fayl qabul qilindi \n♻Data dls o'zgartirildi",reply_markup=ortga_to_panel)
        await message.document.download("data_dls.py",destination_file="")
        await state.finish() 


    if message.content_type == "text":
        if message.text == "🔙 Ortga":
            await message.answer("🔙 Yaxshi orqaga qaytildi",reply_markup=panel_tugma)
            await state.finish()


@dp.callback_query_handler(text="special_sts")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    message_only= await call.message.answer("😉Biroz kuting...")
    users = db.select_all_users()
    message = f"🤖Botimizda {len(users)}ta obunachi bor.Ular haqida ma'lumot(Bloklamganni o'zi):\n"
    count = 0
    count_x = 1
    count_y = 10
    messages = []
    for user in users:
        try:
            user_data = await bot.get_chat(user[0])
            # print(user_data)
            user_id = user[0]
            username = user_data.username
            bio = user_data.bio
            count += 1

            
            message+=f"""
        {number_to_stick(count)}-foydalanuvchi:
        🆔Foydalanuvchi idsi: <code>{user_id}</code>
        📛Foydalanuvchi nomi: <code>{user_data.first_name}</code>
        🌐Foydalanuvchi useri: @{username}
        📍Foydalanuvchi biosi: <code>{bio}</code>
        """
            users_count = int(len(users))
            remain_user = users_count - count_y
 
            if count == count_y:
                count_x+=1
                count_y+=10
                messages.append(message)
                message = f"{count_x}-qism"






        except Exception as e:
            pass
    if  remain_user == 0:
        pass
    else:
        messages.append(message)
    await message_only.delete()
    for message in messages:        
        await call.message.answer(message)
    await call.message.answer("👨‍💻Admin panelga qaytish",reply_markup=ortga_to_panel) 
@dp.callback_query_handler(text="channel_tools")
async def channel__tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🤙Birini tanlang!",reply_markup=channel_tools)

@dp.callback_query_handler(text="ban_tools")
async def ban__tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🤙Birini tanlang!",reply_markup=ban_tools)
@dp.callback_query_handler(text="data_dls_bot_unmute")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🤙Birini tanlang!",reply_markup=data_dls_bot_unmute)
@dp.callback_query_handler(text="ortga_panel")
async def send_ad_to_all(call: types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Yaxshi ortga qaytildi",reply_markup=panel_tugma)
