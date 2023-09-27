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
            text = f"<b> ○ 🎃 Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n ○ 🤗 Developed by  : <code>@Ktgp_3453</code>\n ○ 😶‍🌫️ Source Code : <a href='https://r.mtdv.me/github-direct-telebot-file'>Click here</a>\n ○ ❤️ Anime Channel : @AnimeXabyss\n ○ 😎 Ongoing Channel : @Ongoing_Anime_Abyss\n ○ 😊 Admin 1 : @Real_Call_Me_Blank\n ○ 🤗 Admin 2 : @Ktgp_3453</b>" ,
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
