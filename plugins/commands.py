import logging
logger = logging.getLogger(__name__)

from translation import Translation
from pyrogram import Client, filters

@Client.on_message(filters.command("userbot_start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply(
        text=Translation.START_TXT,
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_message(filters.command("userbot_help") & filters.private & filters.incoming)
async def help(client, message):
    await message.reply(
        text=Translation.HELP_TXT,
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_message(filters.command("userbot_about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        quote=True
    )

