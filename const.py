"""
File containing constants useful for the project.

Usage:
For `getenv` functions to work, create a file with name `.env` inside the same
directory as `bot.py`.
"""

from os import getenv
from dotenv import load_dotenv

# default keyword for commands
KEYWORD_DEFAULT = '$'

# maximum characters for command keyword
KEYWORD_LENGTH = 5

# ===== consts in env ===== #
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


def _channel_id_maker(key: str) -> int | None:
    try:
        return int(getenv(key))
    except (TypeError, ValueError):
        return None


CHANNEL_DEFAULT = _channel_id_maker("CHANNEL_DEFAULT")
CHANNEL_0 = _channel_id_maker("CHANNEL_0")
