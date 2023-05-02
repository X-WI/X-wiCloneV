import os
from config import Config
from translation import Translation
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@Client.on_message(filters.command('start') & filters.user(Config.ADMINS))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton('📜 Channel', url='https://t.me/Lx0980_Official'),
        InlineKeyboardButton('Owner ♻️', url='https://t.me/Lx_0980')
    ],[
        InlineKeyboardButton('SouceCode 💡', url='https://github.com/Lx0988')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name),
        parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command('help') & filters.user(Config.ADMINS))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.HELP_TXT,
        parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command('about') & filters.user(Config.ADMINS))
async def about(client, message):
    buttons = [[
        InlineKeyboardButton('💡 SouceCode', url='https://github.com/Sh-Jil/Forwardit'),
        InlineKeyboardButton('close 🔐', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.ABOUT_TXT,
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML
    )


@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
        
