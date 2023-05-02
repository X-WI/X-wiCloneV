import os, asyncio, logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from config import Config 

media_filter = filters.document | filters.video 
caption_text = "➠ @Hollywood_0980\n➠ @DFF_UPDATES"

@Client.on_message(filters.chat(-1001667023505) & media_filter)
async def forward(bot, update):
    try:      
        caption_text = "➠ @Hollywood_0980\n➠ @DFF_UPDATES"
        await bot.copy_message(
            chat_id=-1001556192813, 
            from_chat_id=-1001667023505, 
            message_id=update.id, 
            caption=f"**{update.caption}**" + '\n\n' + f"**{caption_text}**",          
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
