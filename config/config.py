import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "18000")
)  # Remember to give value in Seconds

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "7297381612").split())
)  # Input type must be interger

# You'll need a Private Group ID for this.
LOGGER_ID = int(getenv("LOG_GROUP_ID", ""))

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "ANNIElogs.txt"
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []
