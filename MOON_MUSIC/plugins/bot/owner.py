from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MOON_MUSIC import app
from config import BOT_USERNAME
from MOON_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
ϻσση sʜɪηɪηɢ (@Moonshining3)

ᴛʜᴧηᴋ ʏσυ ᴛσ єᴠєꝛʏσηє ᴡʜσ ᴧᴅᴅєᴅ ϻʏ ʙσᴛs (@musicXanime_bot, @im_kitty_bot, @Kitty_musicXbot, @FIX_X_MUSIC_BOT) ᴛσ ᴛʜє ɢꝛσυᴘs! ɪ ꝛєᴧʟʟʏ ᴧᴘᴘꝛєᴄɪᴧᴛє ʏσυꝛ sυᴘᴘσꝛᴛ. Єηᴊσʏ ᴛʜє ϻυsɪᴄ ᴧηᴅ ʜᴧᴠє ғυη!
ᴋєєᴘ sʜɪηɪηɢ!

Ꝛєɢᴧꝛᴅs,  
sʜᴧʏᴧꝛɪ: @shayariAlfaazonKaAaina
@grandxmasti ᴧηᴅ @kittyxupdates
**
"""

@app.on_message(filters.command("wner", prefixes=["O", "o", "/O"]))
async def start(_, msg):
    buttons = [
        [ 
            InlineKeyboardButton("More information", url="https://t.me/about_ur_moonshining/5")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply(
        text=start_txt,
        reply_markup=reply_markup
    )
