"""
Module containing helper functions for the bot
"""

import discord
from const import *


async def run(c: discord.Client):
    """
    Runs after the initialization of the bot.
    :param c: `Client` object passed from `bot.py`.
     Required by some functions.
    """
    await _send_msg(c, "foo", CHANNEL_0)

# ALL ADDITIONAL FUNCTIONS SHOULD BE HIDDEN #


# ===== HIDDEN FUNCTIONS ===== #
async def _send_msg(c, text: str, channel_id: int):
    """
    Sends a message to a channel with id=`channel_id`.
    :param text: text to be sent.
    :param channel_id: id of target channel. Requires that the target channel is
     in the discord server the bot is active in.
    :raise ValueError: if `channel_id` is not a valid `id`.
    """
    channel = c.get_channel(channel_id)
    if channel is None:
        raise ValueError(
            f'Cannot send message to channel with id "{channel_id}": '
            "the specified channel was not found in discord server")
    await channel.send(text)
