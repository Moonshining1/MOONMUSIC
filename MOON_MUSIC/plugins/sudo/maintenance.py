from pyrogram import filters
from pyrogram.types import Message

from MOON_MUSIC import app
from MOON_MUSIC.misc import SUDOERS
from MOON_MUSIC.utils.database import (
    get_lang,
    is_maintenance,
    maintenance_off,
    maintenance_on,
)
from strings import get_string


@app.on_message(filters.command(["maintenance"]) & SUDOERS)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    
    state = message.text.split(None, 1)[1].strip().lower()
    
    if state == "enable":
        if await is_maintenance():
            return await message.reply_text(_["maint_4"])
        await maintenance_on()
        return await message.reply_text(_["maint_2"].format(app.mention))
    
    elif state == "disable":
        if not await is_maintenance():
            return await message.reply_text(_["maint_5"])
        await maintenance_off()
        return await message.reply_text(_["maint_3"].format(app.mention))
    
    else:
        return await message.reply_text(usage)
