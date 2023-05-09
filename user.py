
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from config import Config, LOGGER
from pyrogram import Client, __version__

import uvloop
uvloop.install()

class Userbot(Client, Config):
    def __init__(self):
        super().__init__(
            "botClient",
            api_hash=self.API_HASH,
            api_id=self.API_ID,
            session_string=self.SESSION,
            workers=20,
            plugins={'root': 'plugins'}
        )

        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        username = "Rentrox"
        if username:            
            await Userbot.send_message(self, chat_id=username, text="Hey bro Now I'm Online")
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
