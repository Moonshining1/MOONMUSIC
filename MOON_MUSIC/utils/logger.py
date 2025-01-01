from pyrogram.enums import ParseMode

from MOON_MUSIC import app
from MOON_MUSIC.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<blockquote><b>❖ {app.mention} ᴘʟᴀʏ ʟᴏɢ ❖</b></blockquote>

<blockquote><b>● ᴄʜᴀᴛ ɪᴅ ➠</b> <code>{message.chat.id}</code>
<b>● ᴄʜᴀᴛ ɴᴀᴍᴇ ➠</b> {message.chat.title}
<b>● ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.chat.username}</blockquote>

<blockquote><b>● ᴜsᴇʀ ɪᴅ ➠</b> <code>{message.from_user.id}</code>
<b>● ɴᴀᴍᴇ ➠</b> {message.from_user.mention}
<b>● ᴜsᴇʀɴᴀᴍᴇ ➠</b> @{message.from_user.username}</blockquote>

<blockquote><b>● ǫᴜᴇʀʏ ➠</b> {message.text.split(None, 1)[1]}
<b>● sᴛʀᴇᴀᴍᴛʏᴘᴇ ➠</b> {streamtype}</blockquote>"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return