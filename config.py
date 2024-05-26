import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27972068")
    API_HASH  = os.environ.get("API_HASH", "6e7e2f5cdddba536b8e603b3155223c1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7134890448:AAHunycfH2NgBb1MvZAhu-nIWq0CkwCHSyg") 
    BOT_USERNAME = os.environ.get('BOT_USERNAME', "The_Hell_King_Renamer_BOt")
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://subhadeepsamui79:v3REnnLOfITn2p8t@cluster0.4z3invg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    BOT_PIC = os.environ.get("BOT_PIC", "https://telegra.ph/file/eb40dba65af97f14fd1e6.jpg")
    OWNER = int(os.environ.get("OWNER", "6075512585"))

    # channels logs
    FORCE_SUBS = os.environ.get("FORCE_SUBS", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002041484396"))
    STRING = os.environ.get("STRING", "BQGq0eQAnRvw3copJFGVlgz-bMwAI3dgK4ak5E6WBdo5z7mFvUtwbKvzlnMH1gG7glM8GZFOXYj-LW8xBS1LNXLNIFLaQI7E_jqbKX0DFvL5xjb-hj4CLbLogQhpJ3nDtrTwoP38zOnfN65qT3zzmXI1QoDnmfcnp0DGstu-GpQSWz-1wKAcIPGiGpvkkhFJigNH-TMZFe1mAHEBRgXcDFhyQvzXpDn7MXCgmVDoCV0UPTTwMy8Iaeuq4sH7XD6047OELanLubFQVISCzNu43uqtieRwOb3HWkEGjvFQWOpXbxZ2YltRGQ7VjtizZH6IB6mhz3JQPawaF5MZKkOyKKlAZlkNaAAAAAFqIPcJAA")
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))






# if you need to add verify system then dm me on telegram
# Check demo bots
# https://t.me/FileRenameXBot
# https://t.me/PremiumRenamerRobot
# https://t.me/FileRenamerXRobot
# token verification adding features is paid so if you want then dm me


# SHORTNER_URL = os.environ.get("SHORTNER_URL", "")
# SHORTNER_API = os.environ.get("SHORTNER_API", "")
# TOKEN_TIMEOUT = os.environ.get("TOKEN_TIMEOUT", "")


# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
