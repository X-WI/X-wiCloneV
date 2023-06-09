"""
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
from config import Config
from translation import Translation

FROM = Config.FROM_CHANNEL
TO = Config.TO_CHANNEL
FILTER = Config.FILTER_TYPE

document = enums.MessagesFilter.VIDEO 

async def fetch_messages(bot, start_id, stop_id):
    async for message in bot.search_messages(chat_id=FROM, filter=document):
        if message.id < start_id or message.id > stop_id:
            # skip the message if it is not in the desired range
            continue
        if message.video:
            file_name = message.video.file_name
        elif message.document:
            file_name = message.document.file_name
        elif message.audio:
            file_name = message.audio.file_name
        else:
            file_name = None               
        await bot.copy_message(
            chat_id=TO,
            from_chat_id=FROM,
            parse_mode=enums.ParseMode.MARKDOWN,       
            caption=message.caption,
            message_id=message.id
        )
        await asyncio.sleep(1)
    return True


@Client.on_message(filters.private & filters.command(["clone"]))
async def clone(bot, message):
    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    
    # Get start and stop message IDs from command
    message_text = message.text.split()
    if len(message_text) < 3:
        await message.reply_text("Please provide start and stop message IDs.")
        return
    start_id = int(message_text[1])
    stop_id = int(message_text[2])
    
    buttons = [[
        InlineKeyboardButton('🚫 STOP', callback_data='stop_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    m = await bot.send_message(
        text="<i>File Forwarding Started😉</i>",
        reply_markup=reply_markup,
        chat_id=message.chat.id
    )

    files_count = 0
    try:
        await fetch_messages(bot, start_id, stop_id)
        files_count += 1
    except Exception as e:
        print(e)
    # await m.delete()
    buttons = [[
        InlineKeyboardButton('📜 Channel', url='https://t.me/Lx0980_Official')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await m.edit(
        text=f"<u><i>Successfully Forwarded</i></u>\n\n<b>Total Forwarded Files:-</b> <code>{files_count}</code> <b>Files</b>\n<b>Thanks For Using Me❤️</b>",
        reply_markup=reply_markup
    )


"""
