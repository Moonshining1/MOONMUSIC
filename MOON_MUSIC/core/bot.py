from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
import config
from ..logging import LOGGER


class MOON(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name="MOON_MUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        # Fetch bot details
        self.id = self.me.id
        self.name = f"{self.me.first_name} {(self.me.last_name or '')}".strip()
        self.username = self.me.username
        self.mention = self.me.mention

        LOGGER(__name__).info(f"Bot Details - ID: {self.id}, Name: {self.name}, Username: @{self.username}")

        # Check LOGGER_ID configuration
        if not config.LOGGER_ID:
            LOGGER(__name__).error("LOGGER_ID is not configured. Please set it in config.")
            exit()

        try:
            LOGGER(__name__).info(f"Attempting to send a start message to LOGGER_ID: {config.LOGGER_ID}")
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot failed to access the log group/channel. Ensure the bot is added and LOGGER_ID is correct."
            )
            exit()
        except ValueError as ve:
            LOGGER(__name__).error(f"Invalid LOGGER_ID provided: {ve}")
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Unexpected error while accessing log group/channel: {type(ex).__name__} - {ex}"
            )
            exit()

        # Check bot's admin status in the log group/channel
        try:
            chat_member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if chat_member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error("Bot is not an admin in the log group/channel. Please promote it.")
                exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Failed to verify bot's admin status in log group/channel: {type(ex).__name__} - {ex}"
            )
            exit()

        LOGGER(__name__).info(f"Music Bot successfully started as {self.name}")

    async def stop(self):
        LOGGER(__name__).info("Stopping Bot...")
        await super().stop()
        LOGGER(__name__).info("Bot has stopped.")


# Main entry point
if __name__ == "__main__":
    LOGGER(__name__).info("Initializing MOON Music Bot...")
    app = MOON()
    app.run()
