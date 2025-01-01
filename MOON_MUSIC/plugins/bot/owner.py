from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MOON_MUSIC import app
from config import BOT_USERNAME
from MOON_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
Moon Shining (@Moonshining3)

Thank you to everyone who added my bots (@musicXanime_bot, @im_kitty_bot, @Kitty_musicXbot, @FIX_X_MUSIC_BOT) to the groups! I really appreciate your support. Enjoy the music and have fun!
Keep shining!

Regards,  
@grandxmasti and @kittyxupdates
**
"""

@app.on_message(filters.command("wner", prefixes=["O", "o", "#"]))
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