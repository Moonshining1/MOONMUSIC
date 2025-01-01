import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors import ButtonUserPrivacyRestricted, BadRequest
from youtubesearchpython.__future__ import VideosSearch

import config
from MOON_MUSIC import app
from MOON_MUSIC.misc import _boot_
from MOON_MUSIC.utils.decorators.language import LanguageStart
from MOON_MUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from MOON_MUSIC.utils.formatters import get_readable_time
from MOON_MUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

NEXIO = [
    "https://files.catbox.moe/jrupn9.jpg",
    "https://files.catbox.moe/5z141p.jpg",
    "https://files.catbox.moe/fnl0h7.jpg",
    "https://files.catbox.moe/1lz1go.jpg",
    "https://files.catbox.moe/avackl.jpg",
    "https://files.catbox.moe/1yrzwz.jpg",
    "https://files.catbox.moe/6y22qw.jpg",
    "https://files.catbox.moe/gnnsf2.jpg",
    "https://files.catbox.moe/ss6r60.jpg",
    "https://files.catbox.moe/yuob18.jpg",
    "https://files.catbox.moe/i9xrrp.jpg",
    "https://files.catbox.moe/a9tx8f.jpg"
    "https://files.catbox.moe/wlt26x.jpg",
    "https://files.catbox.moe/c1lylh.jpg",
    "https://files.catbox.moe/82eymp.jpg",
]

HIMANSHI = [
    "CAACAgUAAxkBAAEBYw5m7G9P80t1_j2B3Yd92giEZl5pUAACDQsAAu5MeVcOK7bEmdSlUB4E",
    "CAACAgUAAxkBAAEBYwxm7G9LVcg14qUcZZA3UW_DD8b5EwACpwsAAo1FeFfhiv4M5X_-sR4E",
    "CAACAgUAAxkBAAEBYwdm7G9B0AQOHXTL2YqQPS_1v9aoKwACGw0AAu3GeVeciSOmGXW1Mx4E",
    "CAACAgUAAxkBAAEBYw9m7G9UNbKd5uykZTX8lZ4Cr8LAzAACrQsAAovseFe_Dx9-6uc6Ux4E",
    "CAACAgUAAxkBAAEBYwpm7G9GSePQOKa6J19IJmN4aQdd6wAC-QoAAmpLeFeIwvGei64Sph4E",
    "CAACAgUAAxkBAAEBYwlm7G9F_WH00zaCrHCrOE0hPNVwzgACGAwAAgLieFfTOC4m1R4KvR4E",
    "CAACAgUAAxkBAAEBYyBm7G-lKV7aHgEF3nJFkAfn56C6cwACgAkAArWleFcq3_E-UPFIzh4E",
    "CAACAgUAAxkBAAEBYw1m7G9NGhPaRs7LQ1qNjukWtqleMgAC9QkAAqeOeFeHI7lMCMruQR4E",
    "CAACAgUAAxkBAAEBYwhm7G9C5a3pRXGlnxmd-bPpk6wPTgACKwoAAqDYeVd8I_IUW4LCkx4E",
    "CAACAgUAAxkBAAEBYyFm7G-rzbXl2VpA37MJevvoJ3712QACbQoAAktbeFfdKoQ_a4J2PR4E",
    "CAACAgUAAxkBAAEBYyJm7G-9KCjUg2MsRKZVTpR_aqn9lwACYA4AAqTycVdmzhfCS8nEPx4E",
    "CAACAgUAAxkBAAEBYyNm7G_FwL1o8EbUs4wtYlMwIxAgCAACDQwAAncPeVe97cDgXeKF4B4E",
]



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name.startswith("help"):
            keyboard = help_pannel(_)
            try:
                await message.reply_sticker(random.choice(HIMANSHI))
                await message.reply_photo(
                    random.choice(NEXIO),
                    caption=_["help_1"].format(config.SUPPORT_CHAT),
                    reply_markup=keyboard,
                )
            except ButtonUserPrivacyRestricted:
                await message.reply_text(
                    "Your privacy settings restrict interaction with inline buttons."
                )
            return
        elif name.startswith("sud"):
            # Handle sudo logic here
            return
        elif name.startswith("inf"):
            # Handle info logic here
            return
    else:
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        try:
            await message.reply_sticker(random.choice(HIMANSHI))
            await message.reply_photo(
                random.choice(NEXIO),
                caption=_["start_2"].format(
                    message.from_user.mention, app.mention, UP, DISK, CPU, RAM, served_users, served_chats
                ),
                reply_markup=InlineKeyboardMarkup(out),
            )
        except ButtonUserPrivacyRestricted:
            await message.reply_text(
                "Your privacy settings restrict interaction with inline buttons."
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    try:
        await message.reply_sticker(random.choice(HIMANSHI))
        await message.reply_photo(
            random.choice(NEXIO),
            caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
            reply_markup=InlineKeyboardMarkup(out),
        )
    except ButtonUserPrivacyRestricted:
        await message.reply_text(
            "Your privacy settings restrict interaction with inline buttons."
        )
    await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except BadRequest:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)
                out = start_panel(_)
                try:
                    await message.reply_sticker(random.choice(HIMANSHI))
                    await message.reply_photo(
                        random.choice(NEXIO),
                        caption=_["start_3"].format(
                            message.from_user.mention,
                            app.mention,
                            message.chat.title,
                            app.mention,
                        ),
                        reply_markup=InlineKeyboardMarkup(out),
                    )
                except ButtonUserPrivacyRestricted:
                    await message.reply_text(
                        "Your privacy settings restrict interaction with inline buttons."
                    )
                await add_served_chat(message.chat.id)
        except Exception as ex:
            print(f"Error: {ex}")
