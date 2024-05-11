# from pyrogram import Client, idle
# from plugins.cb_data import app as Client2
# from config import *



# bot = Client(

#             "Renamer",

#             bot_token=BOT_TOKEN,

#             api_id=API_ID,

#             api_hash=API_HASH,

#             plugins=dict(root='plugins'))
           

#  if STRING:
#      apps = [Client2,bot]
#      for app in apps:
#          app.start()
#      idle()
#      for app in apps:
#          app.stop(port = 8080)
    
#  else:
#      bot.run()



# # Jishu Developer 
# # Don't Remove Credit 🥺
# # Telegram Channel @Madflix_Bots
# # Developer @JishuDeveloper

# from pyrogram import Client, idle
# from plugins.cb_data import app as Client2
# from config import *



# bot = Client(

#            "Renamer",

#            bot_token=BOT_TOKEN,

#            api_id=API_ID,

#            api_hash=API_HASH,

#            plugins=dict(root='plugins'))
           

# if STRING:
#     apps = [Client2,bot]
#     for app in apps:
#         app.start()
#     idle()
#     for app in apps:
#         app.stop()
    
# else:
#     bot.run()



# # Jishu Developer 
# # Don't Remove Credit 🥺
# # Telegram Channel @Madflix_Bots
# # Developer @JishuDeveloper


from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()     
        print(f"{me.first_name} Is Started.....✨️")
        
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL, f"**{me.mention} Is Restarted !!**\n\n📅 Date : `{date}`\n⏰ Time : `{time}`\n🌐 Timezone : `Asia/Kolkata`\n\n🉐 Version : `v{__version__} (Layer {layer})`</b>")                                
            except:
                print("Please Make This Is Admin In Your Log Channel")

Bot().run()






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper



# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
