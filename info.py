import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#--------------------------------- ʙoᴛ sᴇᴛᴛɪɴɢs ----------------------------------

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

#-------------------------------- ʙoᴛ ɪɴғoʀᴍᴀᴛɪᴏɴ ---------------------------------

SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '25061703'))
API_HASH = environ.get('API_HASH', '744a017a9c53f3ab489ea0bfa0ffce3f')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

#---------------------------- sᴛᴀʀᴛ ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴀcᴛɪoɴs ----------------------------

REACTIONS = ["🦋",, "🤝", "😇", "🤗", "😍", "😎",  "👍", "🌚", "🎅", "😁", "😐", "🥰", "🤩", "😈", "😱", "🤣", "😘", "👏", "😛", "🎉", "⚡️", "🫡", "🤓", "🏆", "🔥", "🤭", "🆒", "👻"] # ᴅoɴ'ᴛ ᴀᴅᴅ ᴀɴʏ ᴇᴍojɪ ʙᴇcᴀᴜsᴇ ᴛɢ ɴᴏᴛ sᴜᴘᴘoʀᴛ ᴀʟʟ ᴇᴍojɪ

#---------------------------------- ɪᴍᴀɢᴇs ʟɪɴᴋ -----------------------------------

# sᴛᴀʀᴛ ɪᴍᴀɢᴇs ʟɪɴᴋ 
PICS = (environ.get('PICS', 'https://telegra.ph/file/6a0726f79acd8300e9a04.jpg https://telegra.ph/file/68289fefb76dbc43b766d.jpg https://telegra.ph/file/0caad29c0cf91c23fb1b6.jpg https://telegra.ph/file/8c34c755dd16581c1c6b5.jpg https://telegra.ph/file/365e35b554e5a3ea83857.jpg https://telegra.ph/file/07f185825c5b7bfd6fbfb.jpg https://telegra.ph/file/85f95494565a762edb3e7.jpg https://telegra.ph/file/708a1d6ce805fcc6a46d0.jpg https://telegra.ph/file/d799c1a964f211028cc97.jpg https://telegra.ph/file/b987425b80bca0cf45c7e.jpg https://telegra.ph/file/2a8b3779760289b76de24.jpg https://telegra.ph/file/47961be968719b3e24cf0.jpg https://telegra.ph/file/2e127b0f6b1810d733c09.jpg https://telegra.ph/file/281b18770a43a29120252.jpg https://telegra.ph/file/2086dd2aa8382e758a599.jpg https://telegra.ph/file/fcc849db4bf5c517f0f8d.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")

#---------------------------------- ɪᴅ --------------------------------------------

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]

CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002311110539').split()]

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002287323098'))

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]

AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1002386346176')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = [int(auth_channel) for auth_channel in environ.get('AUTH_CHANNEL', '').split() if id_pattern.search(auth_channel)]
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002386346176')

reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002447765352')

DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002311110539')).split()]

REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

#---------------------------- ᴍoɴɢoᴅʙ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ----------------------------------

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://bipinmfp07:OmodwqrRcvV6lrV4@cluster0.2t7so.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

MULTIPLE_DATABASE = is_enabled('MULTIPLE_DATABASE', 'False')
SECONDDB_URI = environ.get('SECONDDB_URI', None)

DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#-------------------------------- sʜᴏʀᴛʟɪɴᴋ --------------------------------------
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)

IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/")
VERIFY2_URL = environ.get('VERIFY2_URL', "")
VERIFY2_API = environ.get('VERIFY2_API', "")

#---------------------------------- ʟɪɴᴋ ---------------------------------------

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Ni_Movie_Request_Group')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Ni_Movies')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Ni_Movies')

#---------------------------------- oᴛʜᴇʀ ---------------------------------------

MAX_B_TN = environ.get("MAX_B_TN", "7")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', '...👻')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

#----------------------------- sᴇᴛ ᴛʀᴜᴇ ᴏʀ ꜰᴀʟsᴇ --------------------------------

P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'False')), False)

#---------------------------- ᴏɴʟɪɴᴇ sᴛʀᴇᴀᴍ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ---------------------------

STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # sᴇᴛ True ᴏʀ False
                                # sᴇᴛ sᴛʀᴇᴀᴍ ᴍoᴅᴇ "True" ᴛʜᴇɴ, ᴍᴜsᴛ ғɪʟʟ ᴜʀʟ !!                  
MULTI_CLIENT = False                        
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "") 


#------------------------------------ ᴛʜᴀɴᴋs ᴛo ------------------------------------

# ᴛʜᴀɴᴋ ʏᴏᴜ ɴɪxʙᴏᴛz™ ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
# ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ 
# ᴄʀᴇᴅɪᴛ - @NIXBOTZ
# ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
# ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ/ᴅᴏᴜʙᴛ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ oɴ ᴛᴇʟᴇɢʀᴀᴍ - @IM_NISHANTT

#-----------------------------------••••••••••••••••-------------------------------
