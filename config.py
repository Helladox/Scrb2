# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "22581733"))
API_HASH = getenv("API_HASH", "1db7bdcf908100cc641c6a5276765c3d")
BOT_TOKEN = getenv("BOT_TOKEN", "7839616256:AAFmadELYRPaku1kHBNW7Kb23VOZ-TiMGLE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6530997270").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rathourayush444:UOtUanJ8fbXqLMjB@cluster0.3anxc25.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002294532244")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002487777733"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
