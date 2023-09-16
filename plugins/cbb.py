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
            text = f"<b> ○ Creator : <a href='tg://user?id={1787248836}'>This Person</a>\n ○ Language : <code>Python3 & Pyrogram</code>\n ○ Source Code : <a href='https://r.mtdv.me/github-direct-telebot-file'>Click here</a>\n ○ Anime Channel : @Otaku_Library\n ○ Chat Group : @Otaku_Chats\n ○ ADMIN1 : @Psycho_Gecko\n ○ ADMIN2 : @Ktgp_3453\n ○ ADMIN3 : @Otaku_Helper</b>" ,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ Close", callback_data = "close")
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
