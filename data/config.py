from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
BOT_START_DAY = env.str("BOT_START_DAY")
try:
	BOT_NAME = env.str("BOT_NAME")
	BOT_NAME = "@" + BOT_NAME
except:
	BOT_NAME = None
	






