"""
File containing constants useful for the project.

Usage:
For `getenv` functions to work, create a file with name `.env` inside the same
directory as `bot.py`.
"""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Discord token: private static token unique to the bot.
# get from dev portal: Settings > Bot > TOKEN
TOKEN = getenv('TOKEN')

# Name of guild: the public name of target Discord server.
GUILD = getenv('GUILD')

# ===== Discord channels ===== #
# Channel id
# `None` if `getenv` does not return an `int`
# get from right-clicking channel > "Copy Server ID" with dev tools enabled
try:
    CHANNEL_0 = int(getenv('CHANNEL_0'))
except (TypeError, ValueError):
    CHANNEL_0 = None
