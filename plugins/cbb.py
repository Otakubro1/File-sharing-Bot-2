#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 🎃 Owner : @The_Strawhat_Luffy\n○ ❤️ Anime Channel : @AnimeXabyss\n○ 😎 Ongoing Channel : <a href='https://t.me/Ongoing_Anime_Abyss'>Redirect ↗️</a>\n○ 🤗 Developed by  : @Ktgp_3453\n○ 😶‍🌫️ Source Code : <a href='https://r.mtdv.me/github-direct-telebot-file'>Click here</a></b>" ,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ Close ❌", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
