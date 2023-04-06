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
            text = f"<b> ○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n ○ Admin 1 : <a href='tg://user?id={CADMIN1}'>View Profile</a>\n ○ Admin 2 : <a href='tg://user?id={CADMIN2}'>Admin 2</a>\n ○ Language : <code>Python3 & Pyrogram</code>\n ○ Channel : @Otaku_Library\n ○ Chat Group : @Otaku_Chats</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
