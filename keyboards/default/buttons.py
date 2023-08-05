from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
buttons = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("🔍Futbolchi ismi yoki familiyasiga ko'ra topish"),

    ],
    [
        KeyboardButton("🔎Uning statistikasi bo'yicha topish!"),
    ],

    [

        KeyboardButton("📞 Admin bilan muloqot"),
        KeyboardButton("📊 Statistika")
    ],
],resize_keyboard=True)


button_back = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("🔙 Ortga"),

    ],
],resize_keyboard=True)



inline_adminrply =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔁 Javob yozish", callback_data="adminusermsg"),
        InlineKeyboardButton(text="🔕 Xabarni bekor qilish", callback_data="cancelled")
        
    ],
    [
        InlineKeyboardButton(text="❌ Ban berish",callback_data="ban"),
        InlineKeyboardButton(text="👨‍💻 Admin Panel", callback_data="admin_panel")
    ]
]
)
inline_userrply =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔁 Javob yozish", callback_data="useradminmsg"),


        
    ]]
)

admin_tugma =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="👨‍💻 Admin Panel", callback_data="admin_panel")
        
    ]]
)


ortga_to_panel =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_panel")        
    ]]
)

panel_tugma = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📩 Reklama & 👤Userga xabar", callback_data="rek_user_message"),
        InlineKeyboardButton(text="⚙️ Kanal sozlamalari", callback_data="channel_tools")

    ],
    [
        InlineKeyboardButton(text="🚷Ban sozlamalari", callback_data="ban_tools"),
        InlineKeyboardButton(text="🔐DBni yuklash",callback_data="download_db")
    ],
    [
        InlineKeyboardButton(text="🤖Bot ✅on/❌off",callback_data="bot_on_off"),
        InlineKeyboardButton(text="🎟data_dls.py & Bot unmute",callback_data="data_dls_bot_unmute")

    ],
    [
        InlineKeyboardButton(text="📊Maxsus statistika",callback_data="special_sts")
    ]
]
)
data_dls_bot_unmute = InlineKeyboardMarkup(inline_keyboard=[
    [

        InlineKeyboardButton(text="♻Futbolchilar bazasini o'zgartirish",callback_data="change_data_dls"),
        InlineKeyboardButton(text="🔔Bot yonish userlarga ma'lumot",callback_data="muted")

    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_panel")     
    ]
])
channel_tools = InlineKeyboardMarkup(inline_keyboard=[
    [

        InlineKeyboardButton(text="➖Kanallarni chiqarib yuborish(Barcha)", callback_data="del_all_channels"),
        InlineKeyboardButton(text=" ➕Kanal qo'shish ", callback_data="new_channel")
    ],
    [

        InlineKeyboardButton(text="➖Kanalni chiqarib yuborish", callback_data="del_channel"),
        InlineKeyboardButton(text="📝Kanallar royhati",callback_data="channels_list")

    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_panel")     
    ]

]

)
ban_tools = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚷Ban qilish", callback_data="ban_man"),
        InlineKeyboardButton(text="⚔️Bandan olish", callback_data="unban_man")
    ],
    [
        InlineKeyboardButton(text="⚔️👥Bandan olish(barcha)", callback_data="unban_men"),
        InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_panel")
    ],
]
)



tugmasi = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="📩Reklama", callback_data="rek_xb"),
        InlineKeyboardButton(text="👤Userga xabar", callback_data="user_xb"),
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_panel")     
    ]
]


)
tugmasi_rek = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💬Forward Xabar", callback_data="forward_xb_rek"),
        InlineKeyboardButton(text="✍️Oddiy Xabar", callback_data="oddiy_xb_rek"),
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_panel")     
    ]
]

)
tugmasi_user = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💬Forward Xabar", callback_data="forward_xb_user"),
        InlineKeyboardButton(text="✍️Oddiy Xabar", callback_data="oddiy_xb_user"),
    ],
    [
        InlineKeyboardButton(text="🔙 Ortga", callback_data="ortga_panel")     
    ]
    
]

)

