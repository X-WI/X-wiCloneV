from pyrogram import Client, enums, __version__
from config import Config, LOGGER
from user import User


class Userbot(Client):     
    def __init__(self):
        super().__init__(
            "filebot",
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=200,
            bot_token=Config.BOT_TOKEN            
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
     
    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Userbot stopped. Bye.")
