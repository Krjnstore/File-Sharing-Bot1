import os
import logging
from logging.handlers import RotatingFileHandler

from os import environ

API = environ.get("API", "fc1ce78ad84b7e6404aac66fe7f9e5c8b369a66f") # shortlink api
URL = environ.get("URL", "linkshortify.com") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/udhvfrf/36") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "Af_Filestore_01_bot") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "25527780"))
API_HASH = os.environ.get("API_HASH", "1ed74b5498913cd53b47063f692abd38")


OWNER_ID = int(os.environ.get("OWNER_ID", "8124792926"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://krjnstore_db_user:5aQswc2gTStwNw5x@cluster0.7rknngk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002557949787"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002534798811"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "43200")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[8124792926]
    for x in (os.environ.get("ADMINS", "8124792926").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !\n\nএখানে কোনো মেসেজ পাঠাবেন না। লিংক পাওয়ার জন্য নিচে দেওয়া চ্যানেলে জয়েন করুন\n\n apko link pane ke liye channel per join karna hoga\n\nChannel link @ainfilm"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel\n\nভিডিও পাওয়ার জন্য আপনাকে আমদের চ্যানেলে জয়েন করতে হবে\n\nvideo ke liye appko backup Channel per join karna hoga</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(8124792926)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
