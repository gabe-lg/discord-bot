"""
Module containing helper functions for the bot
"""

import discord
from const import *


async def init(c: discord.Client):
    """
    Runs after the initialization of the bot.
    :param c: `Client` object passed from `bot.py`.
     Required by some functions.
    """
    await send_msg(c, "foo")


async def send_msg(c, text: str, channel_id: int = CHANNEL_DEFAULT):
    """
    Sends a message to a channel with id=`channel_id`.
    :param c:
    :param text: text to be sent.
    :param channel_id: id of target channel. Requires that the target channel is
     in the discord server the bot is active in.
     Default: `CHANNEL_DEFAULT`
    :raise ValueError: if `channel_id` is not a valid `id`.
    """
    channel = c.get_channel(channel_id)
    if channel is None:
        raise ValueError(
            f'Cannot send message to channel with id "{channel_id}": '
            "the specified channel was not found in discord server")
    await channel.send(text)
