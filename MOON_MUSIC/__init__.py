from MOON_MUSIC.core.bot import MOON
from MOON_MUSIC.core.dir import dirr
from MOON_MUSIC.core.git import git
from MOON_MUSIC.core.userbot import Userbot
from MOON_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = MOON()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
