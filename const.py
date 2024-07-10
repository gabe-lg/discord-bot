"""
File containing constants useful for the project.

Usage:
For `getenv` functions to work, create a file with name `.env` inside the same
directory as `bot.py`.
"""

from os import getenv
from dotenv import load_dotenv


def _id_maker(key: str) -> int | None:
    """
    Helper function: converts a `str` with into `int`.
    :return: an `int` if `key` can be converted into an `int`, otherwise `None`.
    """
    try:
        return int(getenv(key))
    except (TypeError, ValueError):
        return None


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

# User ID
# `None` if `getenv` does not return an `int`
# get from discord app: User Settings > My Account > "Copy Server ID" with dev
# tools enabled
USER_ID = _id_maker("USER_ID")

# ===== Discord channels ===== #
# Channel id
# `None` if `getenv` does not return an `int`
# get from right-clicking channel > "Copy Server ID" with dev tools enabled

CH_ALERTS = _id_maker("CH_ALERTS")
CH_0 = _id_maker("CH_0")

VC_DEFAULT = _id_maker("VC_DEFAULT")
VC_0 = _id_maker("VC_0")
