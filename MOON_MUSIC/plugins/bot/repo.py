from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MOON_MUSIC import app
from config import BOT_USERNAME
from MOON_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ ɪɴᴄʀɪᴄɪʙʟᴇ ʀᴇᴘᴏs ⌾
 
◎ ʙʜᴀɢ ʙʜᴏsᴅɪᴋᴇ
 
◎ ʀᴇᴘᴏ ᴛᴏ ɴᴀ ᴅᴜɴɢᴀ ( repo lene ke liye dm kro @moonshining3 )
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/Kittyxupdates"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/about_ur_moonshining/5"),
          ],
               [
                InlineKeyboardButton("• ɢʀᴀɴᴅ ᴍᴀsᴛɪ •", url=f"https://t.me/grandxmasti"),
],
[
InlineKeyboardButton("• ᴏғғɪᴄɪᴀʟ ʙᴏᴛ •", url=f"https://t.me/musicXanime_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/0wtv2m.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
