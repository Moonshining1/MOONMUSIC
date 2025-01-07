from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from MOON_MUSIC import app

class BUTTONS(object):
    BBUTTON = [
        [
            InlineKeyboardButton("ᴧɪ | ᴄʜᴧᴛɢᴘᴛ", callback_data="TOOL_BACK HELP_01"),
        ],
        [
            InlineKeyboardButton("sєᴧʀᴄʜ", callback_data="TOOL_BACK HELP_02"),
            InlineKeyboardButton("ᴛᴛs", callback_data="TOOL_BACK HELP_03"),
            InlineKeyboardButton("ɪηғσ", callback_data="TOOL_BACK HELP_04"),
        ],
        [
            InlineKeyboardButton("ғσηᴛ", callback_data="TOOL_BACK HELP_05"),
            InlineKeyboardButton("ϻᴧᴛʜ", callback_data="TOOL_BACK HELP_06"),
            InlineKeyboardButton("ᴛᴧɢᴧʟʟ", callback_data="TOOL_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("ɪϻᴧɢє", callback_data="TOOL_BACK HELP_08"),
            InlineKeyboardButton("ʜᴧsᴛᴧɢ", callback_data="TOOL_BACK HELP_09"),
            InlineKeyboardButton("sᴛɪᴄᴋєʀs", callback_data="TOOL_BACK HELP_10"),
        ],
        [
            InlineKeyboardButton("ғυη", callback_data="TOOL_BACK HELP_11"),
            InlineKeyboardButton("ǫυσᴛʟʏ", callback_data="TOOL_BACK HELP_12"),
            InlineKeyboardButton("ᴛ-ᴅ", callback_data="TOOL_BACK HELP_13"),
        ],
        [   
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"),]
        ]
    
    MBUTTON = [
                [
            InlineKeyboardButton("єxᴛʀᴧ", callback_data="MANAGEMENT_BACK HELP_25"),
        ],
        [
            InlineKeyboardButton("ʙᴧη", callback_data="MANAGEMENT_BACK HELP_14"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="MANAGEMENT_BACK HELP_15"),
            InlineKeyboardButton("ϻυᴛє", callback_data="MANAGEMENT_BACK HELP_16"),
        ],
        [
            InlineKeyboardButton("ᴘɪη", callback_data="MANAGEMENT_BACK HELP_17"),
            InlineKeyboardButton("sᴛᴧғғ", callback_data="MANAGEMENT_BACK HELP_18"),
            InlineKeyboardButton("sєᴛ-υᴘ", callback_data="MANAGEMENT_BACK HELP_19"),
        ],
        [
            InlineKeyboardButton("ᴢσϻʙɪє", callback_data="MANAGEMENT_BACK HELP_20"),
            InlineKeyboardButton("ɢᴧϻє", callback_data="MANAGEMENT_BACK HELP_21"),
            InlineKeyboardButton("ɪϻᴘσsᴛєʀ", callback_data="MANAGEMENT_BACK HELP_22"),
        ],
        [
            InlineKeyboardButton("sɢ", callback_data="MANAGEMENT_BACK HELP_23"),
            InlineKeyboardButton("ᴛʀ", callback_data="MANAGEMENT_BACK HELP_24"),
            InlineKeyboardButton("ɢʀᴧᴘʜ", callback_data="MANAGEMENT_BACK HELP_26"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"), 
        ]
        ]
    PBUTTON = [
        [
            InlineKeyboardButton("˹ 🇲σ᭡፝֟ɳ🌙 ˼", url="https://t.me/about_ur_moonshining/5"),
            InlineKeyboardButton("˹ σᴡηєꝛ's ᴄʟᴧη 🎄 ˼", url="https://t.me/Grandxmasti"),
        ],
        [
            InlineKeyboardButton("˹ ʜєʟᴘ ˼", callback_data="MAIN_CP"),
            InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("• ᴧηηɪє ᴠ2.0 •", callback_data="GUIDEBOT_CP"),
            
        ],        
        [
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/grandxmasti"),
            InlineKeyboardButton("˹ σᴡηєꝛ ˼",  callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton("˹ ʙᴧsɪᴄ ɢυɪᴅє  ˼", callback_data="MAIN_BACK HELP_ABOUT"),
            InlineKeyboardButton("˹ sσυꝛᴄє ˼", url="https://t.me/Kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
        [
            InlineKeyboardButton("˹ ϻυsɪᴄ ˼", callback_data="settings_back_helper"),
            InlineKeyboardButton("˹ ϻᴧηᴧɢєϻєηᴛ ˼", callback_data="MANAGEMENT_CP"),
        ],
        [
            InlineKeyboardButton("˹ ᴛσσʟs ˼", callback_data="TOOL_CP"),
            InlineKeyboardButton("˹ ɢᴧʟᴧxʏ ˼", callback_data="GALAXYBOT_CP"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]

    GBUTTON = [
        [
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/Grandxmasti"),
            InlineKeyboardButton("˹ σᴡηєꝛ ˼",  callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton("˹ ɢᴧʟᴧxʏ ˼", callback_data="GALAXYBOT_CP"),
            InlineKeyboardButton("˹ sσυꝛᴄє ˼", url="https://t.me/Kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]

    LBUTTON = [
        [
            InlineKeyboardButton("˹ sʜʏᴧꝛɪ ˼", url="https://t.me/shayariAlfaazonKaAaina"),
            InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼",  url="https://t.me/grandxmasti"),
        ],
        [
            InlineKeyboardButton("˹ σᴡηєꝛ ˼",  callback_data="PROMOTION_CP"),
            InlineKeyboardButton("˹ sσυꝛᴄє ˼", url="https://t.me/Kittyxupdates"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
